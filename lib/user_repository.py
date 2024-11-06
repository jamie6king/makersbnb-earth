
from lib.database_connection import DatabaseConnection
import hashlib
from lib.user import *

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, name, email, phone_number, password):
        # Hash the password
        binary_password = password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()

        # Store the email and hashed password in the database
        self._connection.execute(
            'INSERT INTO users (name, email, phone_number, hashed_password) VALUES (%s, %s, %s, %s)', [name.title(), email.lower(), phone_number.strip(), hashed_password]
        )

    def check_password(self, email, password_attempt):
        # Hash the password attempt
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        # check whether there is a user in the database with the given email 
        # and a matching password hash, using the SELECT... WHERE statement
        rows = self._connection.execute("SELECT * FROM users WHERE email = %s AND hashed_password = %s", [email, hashed_password_attempt])

        # return if such a user exist
        return len(rows) > 0
    
    def find_by_email(self, email):
        rows = self._connection.execute("SELECT * FROM users WHERE email = %s", [email])
        id = rows[0]['id']
        # email = rows[0]['email']
        hashed_password = rows[0]['hashed_password']
        phone_number = rows[0]['phone_number']
        name = rows[0]['name']
        user = User(id, name, email, phone_number, hashed_password)
        return user
      
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            person = User(row["id"],row["name"],row["email"],row["phone_number"],row["hashed_password"])
            users.append(person)
        return users
    
    def find(self, user_id):
        result = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])
        row = result[0]
        return User(row["id"], row["name"], row["email"], row["phone_number"], row["hashed_password"])

