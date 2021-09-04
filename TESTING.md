# Testing

![Image](static/images/readme/amiresponsive.PNG)

# Table of Contents <a name="home"></a>
1. [Validation Services](#validation)
2. [Errors/Warnings HTML](#html)
3. [Errors/Warnings CSS](#css)
4. [Errors/Warnings JS Hint](#js)
5. [Errors/Warnings PEP8](#pep8)
6. [Speed Test](#speed)
7. [Testing User Experience (UX)](#ux)
8. [Manual Testing](#manual)



# Validation <a name="validation"></a>


* [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate html
    * As there are so many reports please find all the results [Here](static/images/testing/Html)

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS
    * style.css: [view report](static/images/testing/CSS.pdf)

* [JS Hint](https://jshint.com/) - Used to validate JavaScript
    * hmpg.js: [view report](static/images/testing/JSHint.pdf)

* [PEP8 Online Service](http://pep8online.com/) - Used to validate CSS
    * style.css: [view report](static/images/testing/PEP8.pdf)


[Back to Testing](TESTING.md)


# Errors/Warnings HTML <a name="html"></a>


I have a number of errors and warnings that I was unable to resolve as they relate directly to the Jinga templating.

These include:

![Image](static/images/testing/htmlcheck.PNG)

The Base template threw up some issues regarding missing/stray tags but having double check I am satisfied that no tags are left open or missing. I believe this is again attributed to Jinga templating.

I am satisfied that the only remaining errors/warnings are in connected with Jinga templating so I have left unresolved.


[Back to Testing](TESTING.md)


# Errors/Warnings CSS <a name="css"></a>


My CSS was free of errors.

I had the following warning:

![Image](static/images/testing/csscheck.PNG)

As this was part of the W3Schools tutorial and it was a warning as opposed to an error I have left this in place.


[Back to Testing](TESTING.md)


# Errors/Warnings JS Hint <a name="js"></a>


This report didnt highlight any errors or warnings to resolve


# Errors/Warnings PEP8 <a name="pep8"></a>


PEP8 showed a number of errors with length, white space and indentation. 

These have all been resolved.


[Back to Testing](TESTING.md)


# Speed Test <a name="speed"></a>


I used [TinyPNG](https://tinypng.com/) to reduce the size of my images to help with loading speed

![Image](static/images/testing/tinypng.PNG)

I tested the website speed for mobile and desktop and recorded the results

Mobile: 

![Image](static/images/testing/speedmobile.PNG)

Desktop:

![Image](static/images/testing/speeddesktop.PNG)

[Back to Testing](TESTING.md)

# Testing User Experience (UX) <a name="ux"></a>


## First time user goals :

* Easily understand the purpose of the website
    * The purpose of the website is clear from the title and opening welcome statement on the homepage
    * The purpose/background to how the site came about is explained further on the about us page  
* Find info on being Gluten Free
    * There are links to external resources on the about us page 
* Register to create an account
    * Users can register for an account on the Register page
* View recipes and search recipes
    * Recipes can be viewed on the homepage 
    * There is a search function on the main page which searches category, recipe name and ingredients

## Returning/Frequent user goals:

* View recipes and search recipes
    * Recipes can be viewed on the homepage 
    * There is a search function on the main page which searches category, recipe name and ingredients
* See new recipes added by other users
    * All new recipes will be visable on the homepage
    * Recipes added by other users will be visable on the homepage
* Check out Monthy Fav recipe
    * This section is to be manually updated on a monthly basis 
    * A future consideration would be for this to update automatically
* Edit/Delete recipes added
    * Users can edit and delete their recipes from their 'My Recipes' page
* Delete user account
    * Users can delete their accounts from their 'Account Page'
    * There is a prompt to confirm they are sure they wish to delete their account


[Back to Testing](TESTING.md)


# Manual Testing <a name="manual"></a>

* Logged out Navbar
    * All links are working and direct user to the pages that match their name
    * The Gluten Free Kids Logo when clicked directs the user to the homepage correctly

* Footer 
    * The Gluten Free Kids Logo when clicked directs the user to the homepage correctly
    * The social media links all open in a new window
    * As this is a fictional page all social media pages direct to home pages not relevant accounts
    * Back to top button is working correctly and take user back to the start of the page

* Hompage
    * Register button link takes user to the correct page
    * Search bar has been tested using 'chocolate' & 'chicken' and returns cards containing these ingredients
    * Search bar has been tested using 'sprouts' and returns correct flash message and register link
    * Search bar no result register link works and takes the user to the correct page
    * Search bar 'clear' button works correctly and returns all recipe cards
    * Recipe cards reveal button works correctly and reveals recipe details
    * Recipe cards reveal close button correctly closes the reveal

* About Us
    * Sliding images work and slogan slide into place with no issues
    * Buttons to select which slide you want work and select the correct picture and the text slides into place with no issues
    * Glow header glows correctly
    * External links in 'What is Gluten free?' section work properly and links open in new window

* Register Page
    * Prompts are present when requested format is incorrect
    * When existing username/password is used flash message is displayed
    * For security it doesnt sepcify if username or password already exists
    * If username & password meet format reqested and do not already exist then register button works correctly and takes user to account page
    * Link to sign in if you have an existing account works correctly and directs user to log in page

* Log in Page
    * Prompts are present when requested format is incorrect
    * When username/password is incorrect flash message is displayed
    * For security it doesnt sepcify if username or password is incorrect
    * If username & password meet format reqested and are correct then log in button works correctly and takes user to account page
    * Link to register if you dont havr an account works correctly and directs user to register page 

* Account Page
    * Share recipe card link works properly and directs user to add recipe page
    * Amend recipe card link works properly and directs user to my recipes page
    * Delete account link works correctly and opens modal. Modal has been created to double check decision to delete account
    *


[Back to Testing](TESTING.md)