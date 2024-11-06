from lib.availability import Availability

def test_constructs_availability():
    exampledate = Availability(None,"10/12/2024","15/12/2024",1)
    assert exampledate.start_date == "10/12/2024"
    assert exampledate.end_date == "15/12/2024"
    assert exampledate.space_id == 1

def test_availability_formats():
    exampledate = Availability(1,"10/12/2024","15/12/2024",1)
    assert str(exampledate) == "User ID:1,Available from 10/12/2024, to 15/12/2024, space:1"