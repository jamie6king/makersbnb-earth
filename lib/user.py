from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

class User:
    def __init__(self, id, name, email, phone_number, hashed_password):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = hashed_password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.email}, {self.phone_number})"
    
