import os
from flask import (Flask, flash, render_template, redirect,
                   request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
if os.path.exists("env.py"):
    import env

# create an instance of Flask and set it to the variable app
app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBANME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


def get_allergens():
    """
    return an ordered
    list of Allergens
    from the database
    """
    return list(mongo.db.allergens.find().sort("allergen", 1))


@app.route("/")
@app.route("/get_recipes.html")
def get_recipes():
    recipes = list(mongo.db.recipes.find())

    return render_template("get_recipes.html", recipes=recipes)


@app.route("/add_recipe.html", methods=['POST', 'GET'])
def add_recipe():
    allergens = get_allergens()

    if request.method == "POST":
        method_steps = request.form.getlist("meth[]")
        ingredients = request.form.getlist("ing[]")
        image_url = url_for("static", filename="images/noimage.png")
        prep_time = "n/a"
        if request.form.get("image_url"):
            image_url = request.form.get("image_url")

        recipe = {
            "name": request.form.get("recipe_name"),
            "descr": request.form.get("recipe_descr"),
            "added_by": "jonathan",
            "added": "",
            "allergens": request.form.getlist("allergens"),
            "difficulty": request.form.get("difficulty"),
            "serves": request.form.get("serves"),
            "image_url": image_url,
            "ingredients": ingredients,
            "method": method_steps,
            "preptime": request.form.get("prep_time"),
            "cooktime": request.form.get("cook_time"),
            }

        mongo.db.recipes.insert_one(recipe)

    return render_template("add_recipe.html", allergens=allergens)


@app.route("/mycookbook/<username>", methods=['POST', 'GET'])
def mycookbook(username):
    
    if session.get('user'):
        my_recipes = list(mongo.db.recipes.find())
        my_pinned = list(mongo.db.recipes.find())
        return render_template("mycookbook.html",username=session["user"], my_recipes = my_recipes)
    
    # if not auhtenitcated redirect to login page
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

                    my_recipes = []
                    my_pinned = []
                    # try catch here
                    my_recipes = list(mongo.db.recipes.find())
                    my_pinned = list(mongo.db.recipes.find())
                    # end try
                    return render_template("mycookbook.html",username=session["user"],my_recipes=my_recipes, my_pinned = my_pinned)
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