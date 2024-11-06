from lib.database_connection import DatabaseConnection
from lib.booking_requests import Booking_requests   

class BookingRequestsRepository:
    def __init__(self, connection):
     self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM booking_requests')
        all_bookings = []
        for row in rows:
            booking = Booking_requests(row["id"],row["customer_id"],row["start_date"],row["end_date"],row["space_id"],row["owner_id"],row["accepted"])
            all_bookings.append(booking)
        return all_bookings
    
    def find (self,customer_id):
       rows = self._connection.execute(
          'SELECT * FROM Booking_requests WHERE id = %s', [customer_id])
       row = rows[0]
       return Booking_requests(row["id"],row["customer_id"],row["start_date"],row["end_date"],row["space_id"],row["owner_id"],row["accepted"])
    

      ## self._connection.execute('INSERT INTO booking_requests ()')