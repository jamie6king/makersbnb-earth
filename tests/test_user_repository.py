from lib.user_repository import UserRepository
from lib.user import User
from flask_bcrypt import Bcrypt
from flask import Flask

app = Flask(__name__)
bcrypt = Bcrypt(app)

def test_user_repository_starts_empty(db_connection):
    
    db_connection.seed("seeds/makersbnb.sql")

    repository = UserRepository(db_connection)

    users = repository.all()

    assert users == []

def test_create_user(db_connection):
        db_connection.seed("seeds/makersbnb.sql")
        repository = UserRepository(db_connection)

        repository.create(User(None, "bobby", "bobb2fr@gmail.com", "07946477898","qwerty123"))
         
         
        result = repository.all()

        assert len(result) > 0
        user = result[0]
        

        
        assert user.name == "bobby"
        assert user.email == "bobb2fr@gmail.com"
        assert user.phone_number == "07946477898"
        


       


        