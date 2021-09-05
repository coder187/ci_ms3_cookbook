# Covid-19 Tracker
[Link to live site on Heroku](https://ci-cookbook.herokuapp.com/)

[Link to main README.md file](https://github.com/coder187/ci_ms3_cookbook/blob/main/README.md)
                              


Project - Backend Development - Code Institute

## Testing

### W3C Validators
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

*   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/) 
    * [Home Page](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/home.png)
    * [Sign Up](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/register.png)
    * [Login](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/login.png)
    * [My CookBook](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/profile.png)
    * [View Recipe ](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/view_recipe.png)
    * [Add Recipe ](https://raw.githubusercontent.com/coder187/ci_ms3_cookbook/main/supp/images/screenie/add_recipe.png)
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
| Add new blank html page to project | blank page ready for code saved as index.htm | Pass ||
| Add Nav Bar to top of index | Nav Bar should stay at top of page at all screen sizes | Pass ||
| Add Nav Bar Items to Nav Bar | Nav Bar items should collapse to Burger Menu style at small screen sizes | Pass ||
| Add Footer Section | Four equal width columns occupying the full width of the page. | Pass ||
| Add Arcgis logo to left column | Center content within column | Pass ||
| Add data.gov.ie logo to second column | Center content within column | Pass |
| Add data.gov.ie logo to second column | Center content within column | Pass ||
| Add ECDC logo to third column | Center content within column | Pass ||
| Add social links to last column | Center content within column | Pass ||
| Add hyper links to Social Media Icons | Click link opens target in new browser window | Pass ||
| Add hover effect to Social Media Icons | On mouse hover the background fades to green. On mouse out the background fades back to original colour | Pass ||
| Add Header Section which consists of four columns of equal width below Nav Bar | Mobile View: Columns should float directly below each other and align vertically | Pass ||
| Add header section which consists of two columns below Nav Bar| Desktop View: Columns should align horizontally to fit screen. | Pass ||
| Add Covid Cases section which consists of three columns below header section. | Mobile View: Columns should float directly below each other and align vertically | Pass ||
| Add Covid Cases section which consists of three columns below header section. | Desktop View: Center column consumes two thirds of width with the remaining two columns occupying one third each| Pass ||
| Add Vaccine Data section which consists of three columns below Covid section. | Mobile View: Columns should float directly below each other and align vertically | Pass ||
| Add Vaccine Data section which consists of three columns below Covid section. | Desktop View: Columns should align horizontally to fit screen. | Pass ||
| Add Vaccine Chart section which consists of a single column centred on screen below the Vaccine Data section. | Mobile & Desktop View: Columns should float directly below section above with content centred | Pass ||
| On index page load. | Connect to endpoint, read Last Update Field & populate first column| Pass |1|
| On index page load. | Connect to endpoint, read Total Case Number & populate second column| Pass |1|
| On index page load. | Connect to endpoint, read Death field & populate third column| Pass |1|
| On index page load.. | Connect to endpoint, read Cases field & populate last column| Pass |1|
| On index page load. | Connect to endpoint, get list of counties reported & populate second row, first column with a table with a row per County with total cases and percentage of population.| Pass |1|
| On index page load. | Connect to endpoint, retrieve Local Electoral Area Covid Statistics | Pass |1||
| On index page load. | Render interactive map of Rep. of Ireland in center column of second row.| Pass |1||
| On index page load. | Render map legend third column.| Pass |1||
| On page resize. | Map resizes to fit display. Popup docks to lower half of the map element.| Pass |1||
| On page resize. | Legend wraps and aligns below the map.| Pass |1||
| On map left click. | A Popup loads with content from the selected Local Electoral Area | Pass |1||
| Popup Dock.| The Popup Dock icon, when clicked docks the popup to right side of the map element.| Pass |1||
| Popup Dock.| On smaller screens the Popup is responsive, by docking to the lower half of the map window and only displaying the Title area. Clicking the Title opens & closes the rest of the Popup.| Pass |1|
| On Popup Zoom.| The map zooms to the selected LEA| Pass |1|
| On Popup Close.| The Popup closes| Pass |1|
| On Home Icon Click.| Re-center the map| Pass |1|
| On page load. | Load & parse vaccine data.| Pass |2|
| On page load. | Populate vaccine section, column 1 with total First Dose figure.| Pass |2|
| On page load. | Populate vaccine section, column 2 with second Dose figure.| Pass |2|
| On page load. | Populate vaccine section, column 3 with Total Dose administered.| Pass |2|
| On page load. | Render vaccine doughnut chart with two datasets, first & second dose by vaccine type.| Pass |2|
| On page load. | Render vaccine doughnut chart legend.| Pass |2|
| On chart left click. | Display tooltip with content from selected chart data point.| Pass |2|
| On page resize. | Chart resizes in a responsive manner.| Pass |2|
| On no COUNTY data. | display no data message | Pass |1|
| On page load. | Connect to endpoint, read ICU fields and populate ICU table | Pass |1|
| On no ICU data. | display no data message | Pass |1|
| Copy index page and save as sources.html. Remove all content between nav and footer. Update nav items. | new page templated from index.html and ready for code. | Pass ||
| Add a Data Sources section with a single column which consumes the full screen width. | Content should align left. | Pass ||
| Add several unordered lists which align vertically. | Content contains informational text and hyperlinks to data source homepages. | Pass ||
| Copy index page and save as conf.html. Remove all content between nav and footer. Update nav items. | new page templated from index.html and ready for code. | Pass ||
| Add single column to Conf.html with jumbotron element containing success message | Column is responsive to all device sizes.. | Pass ||
| Add button to return to homepage to Conf.html | User is redirected to index.html | Pass ||
| Copy conf.html and save as fail.html. Update nav items. | new page templated from index.html and ready for code. | Pass ||
| Edit content of fail.html to show failure message | Column is responsive to all device sizes.. | Pass ||
| Click button to return to homepage | User is redirected to index.html | Pass ||
| Copy index page and save as signup.html. Remove all content between nav and footer. Update nav items. | new page templated from index.html and ready for code. | Pass ||
| Add two centred columns to the page. | On Mobile: the columns align vertically. | Pass ||
| Add paragraph of text to first column and a signup form to second column. | All fields on the form are required. The email field requires correct formatting. The fields are validated before submission | Pass ||
| Submit the Form by clicking Submit button. | Two emails are sent. One to the email address supplied and the second to the (theoretical) system administrator. | Pass |3|
| Submit the Form by clicking Submit button. | If the email send succeeds the conf.html page loads to display a success message. | Pass ||
| Submit the Form by clicking Submit button. | If the email send fails the fail.html page loads to display a failure message. | Pass ||
| On index page load| Load background audio file. Page audio volume is set to zero by default| Pass ||
| Menu button toggle background audio on/off | Toggle page audio on/off. | Pass ||
| Menu button toggle background audio on/off | Toggle menu item button icon. | Pass ||
| On page load Check for data being returned. | Display "No Data" in corresponding html elements.| Pass |4|
| On page load Check for Error Condition. | Console Log error message and display "error ?" in corresponding html elements.| Pass |1|
| Users who direct to a non-existent page or resource.| The user is redirected back to the main page without having to use browser navigation buttons. | Pass ||


*1. Disruption to the HSE computer systems caused by the cyber-attack has resulted in some dataset updates being paused until further notice.*   
*2. Note: A CORS issue prevented me from reading the vaccine data directly from the host server so I have copied the vaccine data file locally. I will come back to this to rectify.*        
*3. Note: I have used my own email address as the admin address*  
*4. I have noticed during testing over the past number of days that some of the endpoints can return zero rows of data. This may be due to updates being made to the underlying datas sources*
*I have since added a check for zero rows so that I can update the display accordingly.*

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
  