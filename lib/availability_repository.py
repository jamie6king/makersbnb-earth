from lib.database_connection import DatabaseConnection
from lib.availability import Availability

class AvailabilityRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM availability')
        available = []
        for row in rows:
            onhand = Availability(row["id"],row["start_date"],row["end_date"],row["space_id"])
            available.append(onhand)
        return available
    
    def create(self,booking_request):

        self._connection.execute('INSERT INTO availability(start_date, end_date, space_id) VALUES (%s,%s,%s)',[
        booking_request.start_date, booking_request.end_date, booking_request.space_id])

        return None
    
    def find(self, space_id):

        rows = self._connection.execute(
            'SELECT * FROM availability WHERE id = %s', [space_id])
        row = rows[0]
        return Availability(row["id"], row["start_date"], row["end_date"], row["space_id"])
    
