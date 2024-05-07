from flask import Blueprint, render_template, url_for

views = Blueprint(__name__, "views")

@views.route("/home")
def home():
    return render_template("index.html")
