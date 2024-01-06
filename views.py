from flask import Blueprint

views = Blueprint(__name__, "views")


@views.route("/")
def landing():
    return "hello"
    # return redirect(url_for('views.home'))
