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

        repository.create("bobby", "bobb2fr@gmail.com", "07946477898", "qwerty123")
        
        result = repository.all()

        assert len(result) > 0
        user = result[0]
        print(user.password)

        assert user.name == "Bobby"
        assert user.email == "bobb2fr@gmail.com"
        assert user.phone_number == "07946477898"
        assert user.password == "daaad6e5604e8e17bd9f108d91e26afe6281dac8fda0091040a7a6d7bd9b43b5"