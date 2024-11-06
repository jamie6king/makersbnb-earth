from lib.booking_requests import Booking_requests

def test_constructs_booking_request():
    exampledate = Booking_requests(None,1,"10/12/2024","15/12/2024",1,3,True)
    assert exampledate.start_date == "10/12/2024"
    assert exampledate.end_date == "15/12/2024"
    assert exampledate.space_id == 1
    assert exampledate.owner_id == 3
    assert exampledate.accepted == True
    assert exampledate.customer_id == 1

def test_formats_booking_request():
    exampledate = Booking_requests(1,2,"10/12/2024","15/12/2024",1,3,True)
    assert str(exampledate) =="User ID:1,customer_id:2 desired dates:10/12/2024, to 15/12/2024, space:1, owner:3, accepted:True)"