from flask import Blueprint, url_for, render_template, request, redirect

views = Blueprint(__name__, "views")


@views.route("/")
def landing():
    # return "hello"
    return redirect(url_for('views.login_page'))


@views.route("/login")
def login_page():
    return render_template("login.html")


@views.route("/emmaisadoofus")
def emmaisadoofus():
    return "emma is a DOOFUS"
