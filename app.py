import os
from flask import (Flask, flash, render_template, redirect,
                   request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env

# create an instance of Flask and set it to the variable app
app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBANME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


def calc_avg_rating(recipe):
    """
    calculate
    the avergae rating for a given recipe
    and return the avg and the numnber of ratings
    currently in the recipe collection
    """
    # cant figure out to check if field exists
    # using  {"$exists": True}
    # instead trap the error and return
    try:
        ratings = recipe["ratings"]
    except Exception as ex:
        return [0, 0]
    else:
        arr_len = len(ratings)
        if arr_len == 0:
            return [0, 0]

        total = 0
        for rat in ratings:
            total = total + int(rat)
        
        if total != 0:
            avg = total/arr_len
        else:
            avg = 0

        return [int(avg), arr_len]


def get_one_recipe(recipe_id):
    return mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})


def get_top_recipes(count):
    """
    return top(count) recipe from database
    """
    return list(mongo.db.recipes.find().limit(count))


def delete_recipes(recipe_id, user_name):
    """
    delete recipe from database
    if the user_name is supplied
    delete all recipes for that user
    """

    # you must either be an admin
    # or the recipe owner to delete a recipe

    recipe = get_one_recipe(recipe_id)
    recipe_owner = recipe["added_by"]

    if session.get("user") is None:
        return -1

    if session["user"].lower() != recipe_owner.lower() and session["user"] != "admin":
        return -2

    try:
        if user_name:
            print("user")
            print (ObjectId(recipe_id))
            mongo.db.recipes.remove({"added_by": user_name})
        else:
            print("no user")
            print (ObjectId(recipe_id))
            print (recipe_id)
            mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    except:
        # log ex
        return 0
    else:
        return 1

def get_allergens():
    """
    return an ordered
    list of Allergens
    from the database
    """
    return list(mongo.db.allergens.find().sort("allergen", 1))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


@app.route("/")
@app.route("/get_recipes.html")
def get_recipes():
    top_recipes = get_top_recipes(10)
    avgs = []
    for rec in top_recipes:
        avgs.append(
            {
                "id": rec["_id"],
                "noofavg": calc_avg_rating(rec)[1],
                "avg": calc_avg_rating(rec)[0]
            })
    return render_template("get_recipes.html", top_recipes= get_top_recipes(10),avgs=avgs)


@app.route("/search", methods=['POST', 'GET'])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("get_recipes.html", top_recipes=get_top_recipes(10), recipes=recipes)


@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    recipe = get_one_recipe(recipe_id)
    avg = calc_avg_rating(recipe)
    return render_template("view_recipe.html", recipe=recipe, avg=avg)


@app.route("/add_recipe.html", methods=['POST', 'GET'])
def add_recipe():
    # check that the user is logged in
    if not session.get("user"):
        return redirect(url_for("login"))

    if request.method == "POST":
        method_steps = request.form.getlist("meth[]")
        ingredients = request.form.getlist("ing[]")
        image_url = url_for("static", filename="images/noimage.png")
        ratings = []

        now = datetime.now()
        if request.form.get("image_url"):
            image_url = request.form.get("image_url")

        recipe = {
            "name": request.form.get("recipe_name"),
            "descr": request.form.get("recipe_descr"),
            "added_by": session["user"],
            "added": now.strftime("%d %B, %Y %H:%M:%S"),
            "allergens": request.form.getlist("allergens"),
            "difficulty": request.form.get("difficulty"),
            "serves": request.form.get("serves"),
            "image_url": image_url,
            "ingredients": ingredients,
            "method": method_steps,
            "preptime": request.form.get("prep_time"),
            "cooktime": request.form.get("cook_time"),
            "ratings": ratings
            }

        #try catch
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Saved Successfully")
        
    # get allergens list from db
    allergens = get_allergens()
    
    return render_template("add_recipe.html", allergens=allergens)


@app.route("/mycookbook/<username>", methods=['POST', 'GET'])
def mycookbook(username):

    if session.get('user'):
        my_recipes = list(mongo.db.recipes.find({"added_by": session["user"]}))
        # my_pinned = list(mongo.db.recipes.find({"created_by": session["user"]
        #                                       }))
        return render_template("mycookbook.html", username=session["user"],
                               my_recipes=my_recipes)

    # if not auhtenitcated redirect to login page
    return redirect(url_for("login"))


@app.route("/edit_recipe/<recipe_id>", methods=['POST', 'GET'])
def edit_recipe(recipe_id):
    
    if request.method == "POST":

        now = datetime.now()
        method_steps = request.form.getlist("meth[]")
        ingredients = request.form.getlist("ing[]")
        # ratings = request.form.get("ing[]")
        submit = {
            "name": request.form.get("recipe_name"),
            "descr": request.form.get("recipe_descr"),
            "added_by": session["user"],
            "added": now.strftime("%d %B, %Y %H:%M:%S"),
            "allergens": request.form.getlist("allergens"),
            "difficulty": request.form.get("difficulty"),
            "serves": request.form.get("serves"),
            "image_url": request.form.get("image_url"),
            "ingredients": ingredients,
            "method": method_steps,
            "preptime": request.form.get("prep_time"),
            "cooktime": request.form.get("cook_time")
        }

        try:
            mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        except Exception as ex:
            flash("Could Not Reach The Database-Please Try Again Later.")
            # log(ex)
        else:
            flash("Recipe Udated Successfully.")
            return redirect(url_for('mycookbook', username=session["user"]))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    
    difficulty = ["Easy", "Medium", "Hard"]
 
    selected_allergens = recipe["allergens"]    # allergens in this recipe
    not_selected = []                           # allergens not in this recipe
    allergens = get_allergens()                 # all allergens
    for allergen in allergens:
        if not allergen["allergen"] in selected_allergens:
            not_selected.append(allergen["allergen"])

    return render_template("edit_recipe.html", recipe=recipe, selected_allergens=selected_allergens, not_selected=not_selected,difficulty=difficulty)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    res = delete_recipes(recipe_id, "")
    if res > 0:
        flash("Recipe Deleted Successfully")
    else:
        flash("Recipe Delete Failed")

    if res >= 0:
        return redirect(url_for("mycookbook",username=session["user"]))
    elif res == -1:
        flash("You Need To Login To Perform This Action")
        return redirect(url_for("login"))
    else:
        flash("You Need To Be An Admin Or The Recipe Owner To Perform This Action")
        return redirect(url_for("login"))



@app.route("/login.html", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            if check_password_hash(
                existing_user["password"],request.form.get("password")):
                    flash("Welcome, {}".format(request.form.get("username")))
                    session["user"] = request.form.get("username").lower()

                    return redirect(url_for("mycookbook",username=session["user"]))
                    
            else:
                flash("Username and/or Password Incorrect")
        else:
            flash("Username and/or Password Incorrect")

    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/register.html", methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
            }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Reistration Successful")
        return render_template("mycookbook.html",username=session["user"])
    
    return render_template("register.html")


# set host and ip from env.py
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)