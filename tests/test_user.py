from lib.user import User

"""
Test User is created correctly
"""
def test_user_created():
    user = User(1,
                "Test User", 
                "test@gmail.com",
                "12345678910",
                "password")
    assert user.id == 1
    assert user.name == "Test User"
    assert user.email == "test@gmail.com"
    assert user.phone_number == "12345678910"

"""
Test format correct
"""
def test_users_format():
    user = User(1, "Test User",
                "test@gmail.com",
                "12345678910",
                "password")
    assert str(user) == "User(1, Test User, test@gmail.com, 12345678910)"
 