# MyCookBook
[Link to live site on Heroku](https://ci-cookbook.herokuapp.com/)

[Link to main README.md file](https://github.com/coder187/ci_ms3_cookbook/blob/main/README.md)
                              


Project - Backend Development - Code Institute

## Testing

### W3C Validators
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. Please note, that the edit_recipe page has a small number of errors which I believe are due to 1. materialize css and 2. the dynamic creation of controls are runtime. I will come back to fix these.

*   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/) 
    * [Home Page](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/home.png)
    * [Sign Up](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/register.png)
    * [Login](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/login.png)
    * [My CookBook](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/profile.png)
    * [View Recipe ](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/view_recipe.png)
    * [Add Recipe ](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/add_recipe.png)
    * [Edit Recipe ](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/edit.png)
    * [Dashboard](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/dashboard.png)   
    *  [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - [Results](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/css_validate.png)



### Testing planning.
With this project I have use Test [Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) model (TDD).

The TDD method consists of a cycle of :
* write new test
* implement new feature
* run all tests & repeat all steps until all tests pass.

### Implementation

| Action      | Expected Outcome | Result | Note |
| ----------- | ---------------- | -------| -----|
| Add template directory and base page | blank page ready for code saved as base.html | Pass ||
| Add Nav Bar Items to top of page | Nav Bar should stay at top of page at all screen sizes | Pass ||
| Add Nav Bar Items to Nav Bar | Nav Bar items should collapse to Burger Menu style at small screen sizes | Pass ||
| Add Register Account Page. | Password is hased abd record added to Users collectio. Check for existing username prevents duplicate user accounts. | Pass ||
| Add Login Page. | User is authehnticated and session vars are set. | Pass ||
| Add Logout function. | Clear session variables. Users must login to add/edit/delete data. | Pass ||
| Add New Recipe add page. | Form validation prevents bad data being passed to controller. Docunmets are created in the Recipe Collection. User must be logged in to create a recipe | Pass ||
| Add Edit Recipe page. | Recipe ingredients and method steps can be added and removed dynamically. | Pass ||
| Add hero image with overlayed welcome text. | Mobile View: Column should float to left and center on small screens | Pass ||
| Add search bar to center of page. | Mobile View: Search bar floats below welcome text | Pass ||
| Add search results collapsbile control below hero image| Only visible if search executed. | Pass ||
| Add slider section below search results. | Shows top ten recipes by ratings on a continious loop| Pass ||
| Add recipe list collapsible control below slider| The content section shows ratings and number of pinned users.| Pass ||
| Add View Recipe page. | Unauthenticated users can view but must login to rate and and add to favourites. | Pass ||
| Add Rating system. | Authenticated users  may rate a recipe. Ratings are stored as an array in the recioe collection. | Pass ||
| Add Favourites system. | Authenticated users may add and remove recipes from their favourites list. | Pass ||
| Add Favourites system. | The recipe collection maintains an array of users that added that recipe to their favourites. | Pass ||
| Add Favourites system. | A user may remove a recipe from favourites. | Pass ||
| Add Dashboard Page. | Only The admin user may access the dashboard page. | Pass ||
| Add Allergen Add/Delete function. | Only the admin user may add or delete an Allergen entry in the Allergen collection.| Pass ||
| Add Recipe Delete function. | Only the admin user may delete a recipe.| Pass ||
| Add User Delete function. | Only the admin user may delete a user. All recipes created by that user are delete. All pinned items for that user are removed.| Pass ||

### Responsive Design
I tested the site layout using the built in  Chrome Dev Tools with following device emulation:
| Device | Resolution | Throttling | Orientation |
|---------|------------|------------|-------------|
| Moto G4 | 360x640 | None | Portrait|
| Pixel 2 | 411x731 | None | Portrait|
| iPhone 5 | 320x568 | None | Portrait|
| iPad | 768x1024 | None | Portrait|
| iPad | 1024x768 | None | Portrait|
| iPad Pro | 1024x1366 | None | Portrait|
| iPad Pro | 1024x1366 | Mid Tier | Portrait|
| iPad Pro | 1024x1366 | Low End | Portrait|
| Galaxy Fold| 280x653 | None | Portrait|
| Galaxy Fold| 653x280 | None | Landscape|
| Galaxy Fold| 512x717 | None | Portrait|
| Galaxy Fold| 717x512 | None | Landscape|

I tested the site layout using physical devices as follows:
| Device | Browser |Resolution | Throttling | Orientation |
|---------|------------|------------|-------------|--------|
| Samsung A50 on Android 10 | Android Chrome | 412x892 | Cellular / Broadband | Portrait|
| Samsung A50 on Android 10 | Android Chrome | 892x412 | Cellular / Broadband | Landscape|
| Samsung S10 on Android 9 | Android Chrome | 412x869 | Broadband | Portrait |
| Samsung S10 on Android 9 | Android Chrome | 869x412 | Broadband | Portrait |
| HP Laptop on Win 10 Pro 10.0.19041.867 | Chrome 89.0.4389.90| 1366x768 | None |
| HP Laptop on Win 10 Pro 10.0.19041.867 | Chrome 89.0.4389.90| 800x600 | None |
| HP Laptop on Win 10 Pro 10.0.19041.867 | Edge 89.0.774.57 | 1366x768 | None |
| HP zBook on Win 10 Pro 10.0.19041.685 | Chrome 88.0.4324.190 | 1920x1080 | None |

### Testing User Stories from User Experience (UX) Section

#### First Time Visitor Goals
1. As a First Time Visitor, I want to easily understand the main purpose of the site.
    * The website title is clearly displayed in top left of the window, and maintains its position on scroll.
2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
    * The website navigation bar is displayed at the top of all pages.

#### Returning Visitor Goals
3. As a Returning Visitor, I want to see the latest Recipes added.
    * Recipes are searchable by name and description.
4. As a Returning Visitor, I want to view my favourite recipes.
    * Users can pin recipes to their profile for easy retrival later.

#### Frequent User Goals
5. As a Frequent Visitor, I want to view the best rated recipes.
    * Ratings are disaplayed on the recipe card & the top ten recipes are displayed on a slider.
6. As a Frequent Visitor, I want to edit and remove old recipes.
    * Users can edit and delete recipes from their MyCookBook profile page.
7. As a Frequent Visitor, I want to view and compare nutritional data on each recipe.
    * *Not implemented yet.*

  ![](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/us/user_st_1.png)
  ![](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/us/user_st_2.png)   
  ![](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/us/user_st_3.png)   
  ![](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/us/user_st_4.png)
  ![](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/us/user_st_5_profile.png)
  ![](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/us/user_st_6_add.png)
  ![](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/us/user_st_7_edit.png)
  ![](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/us/user_st_8_view1.png)
  ![](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/us/user_st_9_view2.png)
  ![](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/us/user_st_10_dash1.png)
  ![](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/us/user_st_11_dash2.png)


### Further Testing
  * I want to further enhance the error trapping and implement a logging system such that admin users may view a log of activity.
  