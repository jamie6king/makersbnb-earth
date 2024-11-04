class Space:
    def __init__(self, name, description, price,picture_url,user_id, id=None, ):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.picture_url = picture_url
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space ID:{self.id}, Name:{self.name}, Description:{self.description}, Price:{self.price}, Picture URL:{self.picture_url}, User ID:{self.user_id}"