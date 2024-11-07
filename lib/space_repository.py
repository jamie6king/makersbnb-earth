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
    
    def find(self, space_id):
        result = self._connection.execute("SELECT * FROM spaces WHERE id = %s", [space_id])
        row = result[0]

        return Space(row["name"], row["description"], row["price"], row["picture_url"], row["user_id"],row["id"])


    def update(self, new_name, new_description, new_price, new_picture_url, space_id):
        fields = []
        values = []
        if new_name is not None:
            fields.append("name = %s")
            values.append(new_name)
        if new_description is not None:
            fields.append("description = %s")
            values.append(new_description)
        if new_price is not None:
            fields.append("price = %s")
            values.append(new_price)
        if new_picture_url is not None:
            fields.append("picture_url = %s")
            values.append(new_picture_url)

        if fields:
            query = f"UPDATE spaces SET {', '.join(fields)} WHERE id = %s"
            values.append(space_id)
            self._connection.execute(query, values)

        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [space_id])
        row = rows[0]

        return Space(row["name"], row["description"], row["price"], row["picture_url"], row["user_id"],row["id"])
    
    def find_users_spaces(self,user_id ):
        result = self._connection.execute("SELECT * FROM spaces WHERE user_id = %s", [user_id])
        return [ Space(
            space["name"],
            space["description"],
            space["price"],
            space["picture_url"],
            space["user_id"],
            space["id"]
        ) for space in result ]

