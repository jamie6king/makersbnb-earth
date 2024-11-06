from lib.space import Space

def test_space_constructs():
    space = Space("Lakehouse", "Charming lakefront retreat with stunning views, cozy interiors, and private dock access.", 120.99,"https://unsplash.com/photos/brown-house-near-body-of-water-zAjdgNXsMeg",2,1)
    assert space.name == "Lakehouse"
    assert space.description == "Charming lakefront retreat with stunning views, cozy interiors, and private dock access."
    assert space.price == 120.99
    assert space.picture_url == "https://unsplash.com/photos/brown-house-near-body-of-water-zAjdgNXsMeg"
    assert space.id == 1
    assert space.user_id == 2

def test_space_formats_nicely():
    space = Space("Lakehouse", "Charming lakefront retreat with stunning views, cozy interiors, and private dock access.", 120.99,"https://unsplash.com/photos/brown-house-near-body-of-water-zAjdgNXsMeg",2,1)
    assert str(space) == "Space ID: 1, Name: Lakehouse, Description: Charming lakefront retreat with stunning views, cozy interiors, and private dock access., Price: 120.99, Picture URL: https://unsplash.com/photos/brown-house-near-body-of-water-zAjdgNXsMeg, User ID: 2"