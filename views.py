from flask import Blueprint, render_template

views = Blueprint(__name__,"views")

@views.route("/home.html")
def home():
    return render_template("home.html")
@views.route("/about.html")
def about():
    return render_template("about.html")
@views.route("/photos.html")
def photos():
    return render_template("photos.html")