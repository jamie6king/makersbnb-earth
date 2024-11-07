import os
from flask import Flask, render_template, request, session, redirect
from lib.database_connection import get_flask_database_connection
from lib.space_repository import *
from lib.user_repository import *
from lib.user import *
import re
from lib.space_repository import SpaceRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index


@app.route('/', methods=['GET'])
def default_page():
    connection = get_flask_database_connection(app)
    spaceRepo = SpaceRepository(connection)
    userRepo = UserRepository(connection)
    spaces = spaceRepo.all()
    users = userRepo.all()
    return render_template('home.html', spaces=spaces, users=users)

@app.route('/<id>', methods=['GET'])
def get_selected_space(id):
    connection = get_flask_database_connection(app)
    spaceRepo = SpaceRepository(connection)
    userRepo = UserRepository(connection)
    space = spaceRepo.find(id)
    user = userRepo.find(id)
    return render_template("show-space.html", space=space, user=user)

@app.route('/login', methods=['GET'])
def get_login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_attempt():
    email = request.form['email']
    password = request.form['password']

    connection = get_flask_database_connection(app)

    user_repository = UserRepository(connection)

    users = user_repository.all()

    
    
    if user_repository.check_password(email, password):

        return redirect("/logged")
        #return render_template("account_home.html", spaces=spaces)
    else:
        
        return render_template("login.html", error=True, email=email, password=password)


@app.route("/logged", methods=['GET'])
def logged_in():
    connection = get_flask_database_connection(app)
    
    space_respository = SpaceRepository(connection)
    spaces = space_respository.all()

    return render_template("account_home.html", spaces=spaces)


@app.route('/testlogged', methods=['GET'])
def get_logged_page():
    connection = get_flask_database_connection(app)
    space_respository = SpaceRepository(connection)
    spaces = space_respository.all()
    return render_template('account_home.html', spaces=spaces)

@app.route('/signup', methods=['GET'])
def get_signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    country_code = request.form.get('country_code')
    mobile_number = request.form.get('mobile_number')
    
    # Validation: Check if any field is empty
    if not name or not email or not password or not country_code or not mobile_number:
        error = "All fields are required."
        return render_template('signup.html', error=error, name=name, email=email, password=password, country_code=country_code, mobile_number=mobile_number)
    
    # Validation: Check if email format is correct
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        error = "Invalid email format."
        return render_template('signup.html', error=error, name=name, email=email, password=password, country_code=country_code, mobile_number=mobile_number)
    
    # Validation: Check password length (minimum 8 characters)
    if len(password) < 8:
        error = "Password must be at least 8 characters long."
        return render_template('signup.html', error=error, name=name, email=email, password=password, country_code=country_code, mobile_number=mobile_number)
    
    # Validation: Check if mobile number consists only of digits
    if not mobile_number.isdigit():
        error = "Mobile number must contain only digits."
        return render_template('signup.html', error=error, name=name, email=email, password=password, country_code=country_code, mobile_number=mobile_number)
    
    # Combine the country code and mobile number
    phone_number = f"{country_code}{mobile_number}"
    
    # Initialize the database connection and repository
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    # Attempt to create a new user in the database
    try:
        repository.create(name, email, phone_number, password)
        print("User created successfully")
    except Exception as e:
        print(f"Error creating user: {e}")
        error = "An error occurred during signup."
        return render_template('signup.html', error=error, name=name, email=email, password=password, country_code=country_code, mobile_number=mobile_number)

    # Render success template if everything works
    return render_template('signup_success.html')

@app.route("/profile", methods=["GET"])
def get_profile_page():
    return render_template("account-page.html")

@app.route('/list-space', methods=['GET'])
def get_list_space_page():
    return render_template('list-space.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
