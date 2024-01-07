from flask import Blueprint, url_for, render_template, request, redirect, flash

views = Blueprint(__name__, "views")


@views.route("/")
def landing():
    # return "hello"
    return redirect(url_for('views.login_page'))

@views.route("/home")
def home():
    return render_template("home.html")


@views.route("/login", methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == '1234':
            flash('Login successful!', 'success')
            return redirect(url_for('views.home'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')

    return render_template('login.html')


@views.route("/register", methods=['GET', 'POST'])
def register_page():
    return render_template('register.html')


@views.route("/emmaisadoofus")
def emmaisadoofus():
    return "emma is a DOOFUS"
