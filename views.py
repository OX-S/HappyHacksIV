from flask import Blueprint, url_for, render_template, request, redirect, flash
from models import School
from secrets import compare_digest

views = Blueprint(__name__, "views")

schools = [
    School(1, 'School A', 40.123, -74.456, 10000, 2750, "Welcome to School A, a resilient community striving for "
                                                        "excellence despite the challenges we face. Our institution, "
                                                        "with a rich history, grapples with economic and racial "
                                                        "disparities that have left us in need of essential "
                                                        "resources. Your support is crucial in helping us overcome "
                                                        "these challenges. We urgently require basic supplies such as "
                                                        "notebooks, pencils, and art materials to create an "
                                                        "environment where every learner can flourish. Your generous "
                                                        "donation will make a lasting impact and contribute to the "
                                                        "transformation of our educational journey.",
           "images/School_A.jpg"),
    School(2, 'School B', 40.456, -74.789, 15000, 7430, "Welcome to School B, where the pursuit of knowledge knows no "
                                                        "bounds. As students in an historically underfunded school, "
                                                        "we face hurdles that many can't imagine. The lack of "
                                                        "resources hampers our learning experience, but your support "
                                                        "can change that. We urgently need textbooks, calculators, "
                                                        "and science equipment to enhance our education. Your "
                                                        "donation will empower us to overcome challenges and reach "
                                                        "our full potential.", "/images/School_A.jpg"),
    School(3, 'School C', 40.456, -74.789, 7000, 1714, "Greetings from School C, where resilience defines us despite "
                                                       "the obstacles we face. Economic and racial disparities have "
                                                       "left us with limited resources, but our determination to "
                                                       "learn remains unwavering. Your contribution can help bridge "
                                                       "the gap. We are in need of basic classroom supplies, "
                                                       "including backpacks, lunchboxes, and uniforms. Your generous "
                                                       "support will provide us with the essentials we need to focus "
                                                       "on our education and build a brighter future.",
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
