import os
from flask import Flask, render_template, request, session, redirect
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/', methods=['GET'])
def default_page():
    return render_template('home.html')

@app.route('/logged', methods=['GET'])
def get_login_page():
    return render_template('login.html')

@app.route('/logged', methods=['POST'])
def login_attempt():
    return render_template('account_home.html')

@app.route('/signup', methods=['GET'])
def get_signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def get_sign_page():
    return render_template('signup_success.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
