# test database connection
def test_database_connection(db_connection):
    
    # Seed the database with some test data
    db_connection.seed("seeds/database_connection.sql")

    # Insert a new record
    db_connection.execute("INSERT INTO test_table (name) VALUES (%s)", ["second_record"])

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM test_table")

    # Assert that the results are what we expect
    assert result == [
        {"id": 1, "name": "first_record"},
        {"id": 2, "name": "second_record"}
    ]

# test dummy data
def test_database_dummy_data(db_connection):

    db_connection.seed("seeds/makersbnb.sql")
    db_connection.seed("seeds/dummy.sql")

    user_result = db_connection.execute("SELECT * FROM users")
    assert len(user_result) == 5

    spaces_result = db_connection.execute("SELECT * FROM spaces")
    assert len(spaces_result) == 5

    availability_result = db_connection.execute("SELECT * FROM availability")
    assert len(availability_result) == 5

    bookings_result = db_connection.execute("SELECT * FROM booking_requests")
    assert len(bookings_result) == 5