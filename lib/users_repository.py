from lib.users import User


class UsersRepository:
    def __init__(self,connection):
        self._connection = connection
    
    def create(self,user):
        self._connection.execute('INSERT INTO users(name, email,phone_number, password) VALUES (%s,%s)',[
        user.name, user.email, user.phone_number, user.password])

        return None
    