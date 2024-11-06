from lib.database_connection import DatabaseConnection
from lib.space import Space

class SpaceRepository:

    def __init__(self, connection):

        self._connection = connection

    def all(self):
        spaces = self._connection.execute("SELECT * FROM spaces")

        return [ Space(
            space["name"],
            space["description"],
            space["price"],
            space["picture_url"],
            space["user_id"],
            space["id"]
        ) for space in spaces ]

    def create(self, space):

        return self._connection.execute("INSERT INTO spaces (name, description, price, picture_url, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING id", [
            space.name,
            space.description,
            space.price,
            space.picture_url,
            space.user_id
        ])
    

    def find(self, user_id):
        result = self._connection.execute("SELECT * FROM spaces WHERE user_id = %s", [user_id])
        return result.fetchall()

    
