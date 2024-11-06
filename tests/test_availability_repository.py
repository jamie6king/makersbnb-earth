from lib.availability_repository import AvailabilityRepository
from lib.availability import Availability
from datetime import datetime


def test_availability_repository_starts_empty(db_connection):
    
    db_connection.seed("seeds/makersbnb.sql")
    repository = AvailabilityRepository(db_connection)
    onhand = repository.all()
    assert onhand == []

def test_create_date(db_connection):
        db_connection.seed("seeds/makersbnb.sql")
        db_connection.seed("seeds/dummy.sql")
        repository = AvailabilityRepository(db_connection)

        repository.create(Availability(None, "2024/12/10", "2024/12/15",1))
         
         
        result = repository.all()

        assert len(result) > 0
        user = result[5]
        

        
        assert user.start_date == datetime.strptime("2024/12/10", "%Y/%m/%d").date()
        assert user.end_date == datetime.strptime("2024/12/15", "%Y/%m/%d").date()
        assert user.space_id == 1


def test_get_single_date(db_connection):
      db_connection.seed("seeds/makersbnb.sql")
      db_connection.seed("seeds/dummy.sql")
      repository = AvailabilityRepository(db_connection)

      date = repository.find(3)
      print(date)
      assert str(date) == str(Availability(3,'2023-10-12', '2023-10-20', 3))