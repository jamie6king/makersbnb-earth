import os
from flask import Flask, render_template, request, session, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
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
    repo = SpaceRepository(connection)
    spaces = repo.all()
    return render_template('home.html', spaces=spaces)

@app.route('/home/<id>')
def get_selected_space(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    space = repo.find(id)
    return render_template("home/show-space.html", space=space)

@app.route('/logged', methods=['GET'])
def get_login_page():
    return render_template('login.html')

@app.route('/logged', methods=['POST'])
def login_attempt():
    email = request.form['email']
    password = request.form['password']

    connection = get_flask_database_connection(app)

    repository = UserRepository(connection)

    users = repository.all()
    
    for user in users:

        if user.email == email and user.password == password:

            return render_template("account_home.html")

    return render_template("login.html", error=True)

@app.route('/signup', methods=['GET'])
def get_signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def get_sign_page():
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
