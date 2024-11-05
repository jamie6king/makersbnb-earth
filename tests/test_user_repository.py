from lib.user_repository import UserRepository
from lib.user import User

def test_user_repository_starts_empty(db_connection):
    
    db_connection.seed("seeds/makersbnb.sql")

    repository = UserRepository(db_connection)

    users = repository.all()

    assert users == []

def test_create_user(db_connection):
        db_connection.seed("seeds/makersbnb.sql")
        repository = UserRepository(db_connection)

        repository.create(User(None, "bobby", "bobb2fr@gmail.com", "07946477898","password"))
         
         
        result = repository.all()
        assert result == [
              User(1, "bobby", "bobb2fr@gmail.com", "07946477898","password")]



        