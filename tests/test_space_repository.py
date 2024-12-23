from lib.space_repository import SpaceRepository
from lib.space import Space

def test_space_repository_starts_empty(db_connection):
    
    db_connection.seed("seeds/makersbnb.sql")

    repository = SpaceRepository(db_connection)

    spaces = repository.all()

    assert spaces == []

def test_space_repository_create_new_space(db_connection):

    db_connection.seed("seeds/makersbnb.sql")

    repository = SpaceRepository(db_connection)

    space = Space("Test space", "This is a test space.", 69.99, "Picture URL", None, None)
    new_space = repository.create(space)
    space.id = new_space[0]["id"]

    spaces = repository.all()

    assert spaces[0] == space

def test_update_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    db_connection.seed("seeds/dummy.sql")
    repository = SpaceRepository(db_connection)
    repository.update("Lovely Cottage",None,150.0,None,1) 
    updated_space = repository.find(1)
    expected_space = Space("Lovely Cottage", "A charming cottage in the woods, perfect for a weekend getaway.", 150.0, "https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg", 1, 1)
    assert updated_space == expected_space