![Cookbook Image](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/cookbook.png)

# MyCookbook Flask MongoDB CI MS3 App
[Link to live site](https://ci-cookbook.herokuapp.com/)

Project - Python and Data Centric Development - Code Institute

## User Experience (UX)
### Scope
#### User stories
1. As a user I want to easily understand the main purpose of the site.
1. As a user I want to be able to easily navigate throughout the site.#
1. As a user I want to create a user profile.
1. As a user I want to add my own recipes.
1. As a user I want to search the database of recipes.
1. As a user I want to see the nutrional content of each recipe.
1. As the site owner I want to provide links to an external cooking equipment purchasing application.

## Structure
### Technical Capabilities
HTML5, CCS3, Javascript, Python, Flask & MongoDB along with Materializecss framework and are my core strengths in regards to this project.

### Features
  * Responsive on all devices.
  * Individual User Profiles
  * Admin User can add/delete Allergen Data.
  * Admin User can delete Recipes.
  * Admin User can delete User Profiles.
  * Users can add/edit/delete recipes.
  * Users can rate other users recipes.
  * Users can pin other users recipes to the favourites section of their own profile..
  * Search function, search by recipe name and description.
  * Rating system allows users to rate each recipe.

  
   
### Features Left To Implement In Future
  * Ability to import recipe details from another website.
  * Api integration with a service such as Edamam to allow automatic nitrional information to be displayed per recipe.
  * Add Tags or Chips to allow easy recipe tagging and searching.
  * I will refactor the code to use ObjectIds as foreign key fields.
  
  https://developer.edamam.com/
  
### Data Model

**users**  
List of registered users.  
Passwords are hashed.  
The username field is stored in the added_by field of the recipe collection.

| id      | username | email | password |
| ----------- | ---------------- | -------| -----|
| objectid | string | string |string|

**allergens**
List of allergens.  
The allergen text is stored in the recipe collection.
| id      | allergen | 
| ----------- | ---------------- | 
| objectid | string | 

**recipes**
| id     | name |descr | added_by | added | allergens | difficulty | serves | image_url | ingredients| method|prep time|cook time|ratings|pinned|
| ---- | ---- | -------- | -------- | -------- | -------- | -------- | -------- |-------- |-------- |-------- | -------- |-------- | ------|------|
| objectid | string | string | string | string | array(String) |array(String)| string  |array(string) |array(string)|array(string)|string |string| array(String)| array(String)

Note:  
Python arrays persist their order and   
MongoDB Persists the order of [Array type fields](https://docs.mongodb.com/manual/core/document/#document-field-order)

This allows for Method Steps to be stored as an array without needing to store the Step Number.
The steps will always be read back in the same order they were entered.

Each Rating is inserted as an integer to an array in the Ratings field.

Pinned Recipes are stored as an array of usernames in the Pinned field.

## Skeleton

### Wireframes
  * Register Mobile [View](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/wireframes/Register.png)

  * Login Mobile [View](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/wireframes/Login.png)

  * Profile Mobile [View](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/c8867e3d3f2cd9d067ca604fab029a3683e7d507/supp/wireframes/Profile%20(MyCookBook).png)

  * Add/Edit Recipe Mobile [View](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/wireframes/Mobile%20Add_Edit%20Recipe.png)

  * Mobile Recipe [View](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/wireframes/Mobile%20Recipe%20Page.png)
  
  * Mobile Home [View]( https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/wireframes/Mobile%20Home.png)


    Home Page: Main Page with search function & List od all recipes in the system.
    Register. 
    Login Page.
    Profile Page (MyCookBook): List of the users recipes. List of Users pinned recipes.
    Add/Edit/Delete Recipe: Users can add new, edit existing and delete their own recipes.
    Admin Page: Add Edit Allergens List. Delete Recipe. Delete User.
        

## Surface

### Design
  * Colour Scheme	
    I chose green/blue as the main site color palette as I though it matched well with the domain material and hero image.
  * Typography
    Poppins as the main font and Dancing for a little flair. Both from Google Fonts 
   * Imagery
    Hero image of kitchen table with empty notebook helps convey the sites main goal.
    Food and cookery themed icons and images throughout the website help bring the application to life.
  
## Technologies
#### Languages Used
  * HTML5
  * CSS3
  * Javascript
  * Python 3.6
  * Flask
  * Jinja
  * MongoDB
  * Heroku
  

#### Frameworks, Libraries & Programs Used
1. [HTML5](https://www.w3.org/)
1. [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
1. [Javascript](https://www.javascript.com/) 
1. [Materializecss:](https://materializecss.com/)
    - Materializecss was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Prompt' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [GIMP:](https://www.gimp.org/)
    - GIMP 2 was used to resizing & edit images for the website.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
1. [GITPOD:](https://gitpod.io/)
    - GitPod was used to create & debug the html,css, javascript & Python
1. [Google Chrome Dev tools](https://developers.google.com/web/tools/chrome-devtools) 
    - for debugging.
1. [Microsoft Edge](https://www.microsoft.com/en-us/edge) 
    - Dev Tools for testing and debugging.
1. [JShint](https://jshint.com/) 
    - to analyse Javascript code.
1. [SEO CHECKUP](https://seositecheckup.com/)  
    - verify alt tags.
1. [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) 
    - for debugging.
1. [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) 
    - for performance audit.
1. [W3C Markup Validation Service](https://validator.w3.org/)
1. [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/)
1. [Code Institute Course Material](https://codeinstitute.net/)
1. [w3schools](https://www.w3schools.com/) 
    - help with HTML, CSS & Javascript
1. [Stackoverflow](https://stackoverflow.com/) 
    - help with HTML, CSS & Javascript
1. [Slack](https://slack.com/intl/en-ie/) 
    - communication hub with mentor, tutors and fellow students.
1. [Markdown Guide](https://www.markdownguide.org/basic-syntax/) 
    - Markdown Guide for this readme file.
1. [Am I Responsive](http://ami.responsivedesign.is/) 
    - Screen Grab of site on various devices.

## Testing
[Link to Testing.md file]()
Testing
http://pep8online.com/
                          
## Deployment
### Heroku
1. Add requrirements.txt file to project with "pip3 freeze > requiremnets.txt"
1. Add Procfile to project.
1. Push changes to github
1. On HEROKU.com, navigate to the site's repository @ [https://github.com/coder187/ci_ms3_cookbook](https://github.com/coder187/ci_ms3_cookbook)
1. New App
1. Name must be unique.
1. Select Region
1. Deploy - GitHub Connect
1. Select  [https://github.com/coder187/ci-ms3-cookbook](https://github.com/coder187/ci_ms3_cookbook)
1. Connect App
1. Build App.
1. Settings / Reveal Config Vars
1. Add Env.py config variables
1. Select Open App button from Heroku dashboard.


### Deploy Locally via zip file download
1. On GitHub, navigate to the main page of the repository @ [https://github.com/coder187/ci_ms3_cookbook](https://github.com/coder187/ci_ms3_cookbook)
2. Above the list of files, click Code.
![](https://docs.github.com/assets/images/help/repository/code-button.png)
3. Click **Download Zip**
4. Extract the downloaded file to the location where you want the cloned directory.
5. Note: A CORS Plugin may be needed to run the system locally.

## Known Bugs
1. The input text box for the recipe Method on the add recipe page should be larger to accomdate more text.
1. The input text box for the recipe Method on the add recipe page are numbered but they need to be styled so that they more visible.
1. Users can rate the same recipes more than once.
1. Referential Integrity is not enforced for Allergen Delete.
1. Style element embedded to allow narrow margins on home page.

## Credits
### Code
  * Jonathan Kelly for Code Institute Milestone Project Three.
  * Code Institute Courseware
  * [Stackoverflow](https://stackoverflow.com/) for help with debugging css and javascript.
  * [Jinja Docs](https://jinja.palletsprojects.com/) to learn jinja templating and routing.
  * This project takes inspiration from the TaskMan walkthtough project.

### Media
  * I used code from [http://jsfiddle.net/SirusDoma/ayf832td/](http://jsfiddle.net/SirusDoma/ayf832td/) to help with password validation
  * I used images from [Lottiefiles](https://lottiefiles.com/marketplace/the-ultimate-404-error-page) for error pages.
  * Hero image is from [Pexels](https://www.pexels.com/search/cooking/) for error pages.
  * Chefs hat from [Clipart-Library](http://clipart-library.com/free-online-clipart.html).
  * No-Image image from [iStockPhoto.com](https://www.istockphoto.com/).

  
## Data Licensing\Terms of Use
-   Recipes and recipe images were copied from the [BBC Good Food website](https://www.bbcgoodfood.com/).

## Test User Accounts
* Admin User 
    * user:admin
    * password:12345

* Normal User 
    * user:jonathan
    * password:12345

* Normal User 
    * user:sadie
    * password:12345


## Acknowledgements	
-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.

-   
**Please note : this project is for educational use only and was created for the Code Institute Module of Backend Development Milestone Project**

**Created by Jonathan Kelly**