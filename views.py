from flask import Blueprint, url_for, render_template, request, redirect, flash
from models import School
from secrets import compare_digest

views = Blueprint(__name__, "views")

schools = [
    School(1, 'School A', 40.123, -74.456, 10000, 2750, 'Description for School A', "images/School_A.jpg"),
    School(2, 'School B', 40.456, -74.789, 15000, 7430, 'Description for School B', "/images/School_A.jpg"),
    School(3, 'School C', 40.456, -74.789, 7000, 1714, 'This is a longer description for School C to showcase the '
                                                       'truncation of the description in the CSS after 100 chars. '
                                                       'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                                                       'sed do eiusmod tempor incididunt ut labore et dolore magna '
                                                       'aliqua. Ut enim ad minim veniam, quis nostrud exercitation '
                                                       'ullamco laboris',
           "/images/School_A.jpg"),

]


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

        if username == 'admin' and compare_digest(password, '1234'):
            flash('Login successful!', 'success')
            return redirect(url_for('views.home'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'danger')

    return render_template('login.html')


@views.route("/register", methods=['GET', 'POST'])
def register_page():
    return render_template('register.html')


@views.route("/supplies")
def donate_supplies():
    return render_template('supplies.html')


@views.route("/schools")
def school_list_view():
    return render_template('school_list.html', schools=schools)


@views.route('/school/<int:school_id>')
def school_donation_page(school_id):

    selected_school = next((school for school in schools if school.id == school_id), None)

    if selected_school:
        return render_template('donation_page.html', school=selected_school)
    else:
        return 'School not found', 404


@views.route("/emmaisadoofus")
def emmaisadoofus():
    return "emma is a DOOFUS"
