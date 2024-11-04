from lib.database_connection import DatabaseConnection
from lib.users_repository import UsersRepository
from lib.users import User

def db_connection():
    connection = DatabaseConnection()
    connection.seed("seeds/makersbnb.sql")
    return connection

def test_create_user(db_connection):
    def test_create_user(db_connection):
        db_connection.seed("seeds/makersbnb.sql")
        repository = UsersRepository(db_connection)

        repository.create(User(None, "bobby", "bobb2fr@gmail.com", "07946477898", "password"))

  
