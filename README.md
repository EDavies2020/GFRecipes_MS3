# Gluten Free Kids Website


[View live project here](https://dashboard.heroku.com/apps/gf-recipes-ms3/deploy/github)

![Image](static/images/readme/amiresponsive.PNG)

This website has been created for my 3rd milestone, data centric project. 

The site created is a fictional recipe sharing buisness set up by a group of fictional mums, I chose the theme as a mum of a mixed Gluten Free/Normal family so I could relate to the subject I wanted to convey.

Users can register for a free account and then share recipes with other users, they can also edit or delete their recipes and if they've had enough they can delete their account.

## Table of Contents
----------------------

1. Introduction
2. User Experience (UX)
3. Design
4. Wireframes
5. Features

## Introduction
-------------------

### Website Purpose :

* For users to share gluten free recipes
* Allow users to create a account
* Allow users to edit and delete recipes
* Provide information about being gluten free
* Let users know the background to the creation of the site

### Key considerations :

* All recipes must be gluten free, with clear images and instructions
* Website to be bright and colourful but still soft/easy on the eye not garish
* Images to be bright, colourful and relevant
* Layout & content to be child friendly for family to view together

## User Experience (UX)
------------------------

### First time user goals :

* Easily understand the purpose of the website
* Find info on being Gluten Free
* Register to create an account
* View recipes and search recipes

### Returning/Frequent user goals:

* View recipes and search recipes
* See new recipes added by other users
* Check out Monthy Fav recipe
* Edit/Delete recipes added
* Delete user account

### Future considerations :

* Add ratings to each recipe for user to visually identify which recipe is good
* Feedback section - area for user to feedback on site and/or recipes
* Blog for any new GF products/news or events that are relevant

## Design
----------

### Colours:

* I used primary colours and kept it bright so it would grab the attention of children but not so bright it would be off putting for adults
* I wanted the colours to be bright and to appeal to children, to keep their interest when viewing the site with a parent

### Images:

* All non-recipe images were chosen because they were bright, followed the chosen colour scheme and had relevant content 
* Recipe images were sourced from [bbc good food](https://www.bbcgoodfood.com/)
* Non-recipe images were sourced from [unspalsh](https://unsplash.com/) and [pixabay](https://pixabay.com/)
 

### Logo: 
* I used [Jimdo](https://www.jimdo.com/) to create my company logos
* I used cartoon images of children and primary colours to keep with the theme of the site
* I used [favicon.io](https://favicon.io/) to create my favicon for the site

## Wireframes
--------------

### to be uploaded


## Features
--------------

* Navbar/Footer

    * The navbar & footer code came from [Materialize](https://materializecss.com/) 
    * The navbar features the company logo to the left and links to the other pages on the right
    * The navbar switches to a sidebar on smaller screens 
    * Certain links are only visable for registered users
    * The navbar and footer logos share the same colours as the corresponding border
    *The footer has links to social media.<br><b>Note:</b> these links are for the pages main sites as this is a fabricated company
    * The footer also features a return to top button

* Homepage

    * There is a brief introduction to the page followed by a prompt to register for an account
    * There is a monthly fav section showcasing an exsiting recipes and prompts to user to look further
    * There is a search bar which is set to search for words in recipe name, category and ingredients
    * Recipe cards feature a reveal button which displays the timings, ingredients and method

* About Us Page

    * Sliding Carousel featuring captions that slide into place from left/right and center
    * Header has CSS glow effect
    * Links to [wikipedia](https://en.wikipedia.org/wiki/Gluten-free_diet) and [Ceoliac UK](https://www.coeliac.org.uk/information-and-support/living-gluten-free/the-gluten-free-diet/about-gluten/) are provided with information about being gluten free

* Registration/Login pages

    * Both pages ask for a username and password and specify how many characters are required
    * The underline will be red if criteria is not met
    * Flash messages let you know if username/password already exist. It doesnt specify which is incorrect for security purposes
    * There is a link to Login from Registration page if you already have an account and vice versa on Login page

* Account page

    * The account page features a welcome using the users name
    * There is a brief intoduction to you account
    * There are 3 horizontal cards with the following links :
    1. The first card displays a link to add a recipe
    2. The second card displays a link to your recipes page
    3. The third card has link to delet your account. When the link is clicked this triggers a modal to confirm you wish to delete or cancel this request

* Add Recipe Page

    * On this page users can add all the details for your recipe, on each item there is a prompt for the the information required
    * The underline will be red if criteria is not met
    * There is a 'Add Recipe' button which will add the users recipe to the Mongodb database. It will add the recipe to the my recipe page and homepage
    * A flash message will let the user known their recipe has been added

* My Recipes Page

    * Once the users recipes are add they will appear in this section in the same format as the cards on the homepage
    * The cards have 2 floating buttons which are tooltipped to display the purpose of the button when hovered over
    * The edit button takes the user to the edit page where they can amend their recipe
    * The edit recipe form allows the user to save or cancel their changes
    * When changes are made a flash message advises the user that the recipe has been updated
    * The red button allows the user to delete their recipe from the mongodb database
    * The delete button triggers a modal which offers the option to cancel or confirm the request to delete. If delete is selected the record will be deleted permanently 
    
* Logout

    * The Logout link logs the user out of their account
    * When clicked the user is directed to the homepage
    * A flash message will be displayed to let the user know they have been logged out


    






