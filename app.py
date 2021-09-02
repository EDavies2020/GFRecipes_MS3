import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# ======== CONFIG ======== #


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ======== HOME PAGE ======== #


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    # find all recipes from Mongodb
    recipes = list(mongo.db.recipes.find())
    # display for all users
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# ======== ABOUT US ======== #


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


# ======== USER ACTIONS ======== #


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # return message if username/password exists
        if existing_user:
            flash("Username/Password already exists")
            return redirect(url_for("register"))
        # user created if criteria met
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        # registration sucessful message
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("account", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check password matches 
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for(
                        "account", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username/Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username/Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("account.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session
    flash("You have been logged out, see you again soon!")
    session.pop("user")
    return redirect(url_for("get_recipes"))


@app.route("/delete_account/<username>")
def delete_account(username):
    # get session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # if username in session is same delete the account
    mongo.db.users.remove({"username": username.lower()})
    flash("Your account has been deleted")
    session.pop("user")
    return redirect(url_for("register"))


# ======== RECIPE ACTIONS ======== #


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "by": request.form.get("by"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "makes": request.form.get("makes"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "image": request.form.get("image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your recipe has been added!")
        return redirect(url_for("my_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    levels = mongo.db.levels.find().sort("recipe_difficulty", 1)
    return render_template("add_recipe.html", categories=categories, levels=levels)
    

@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "by": request.form.get("by"),
            "recipe_difficulty": request.form.get("recipe_difficulty"),
            "makes": request.form.get("makes"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "ingredients": request.form.get("ingredients"),
            "method": request.form.get("method"),
            "image": request.form.get("image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Your recipe has been updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    levels = mongo.db.levels.find().sort("recipe_difficulty", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories, 
        levels=levels)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Your recipe has been deleted!")
    return redirect(url_for("get_recipes"))


@app.route("/my_recipes")
def my_recipes():
    recipes = list(mongo.db.recipes.find().sort("created_by"))
    return render_template("my_recipes.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

# change to false before submission
