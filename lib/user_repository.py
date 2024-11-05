from lib.user import User
from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)



class UserRepository:
    def __init__(self,connection):
        self._connection = connection
    
    def create(self,user):

        self._connection.execute('INSERT INTO users(name, email, phone_number, password) VALUES (%s,%s,%s,%s)',[
        user.name, user.email, user.phone_number,user.password])

        return None
    

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            person = User(row["id"],row["name"],row["email"],row["phone_number"],row["password"])
            users.append(person)
        return users
    