class Space:
    def __init__(self, name, description, price,picture_url, id=None, ):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.picture_url = picture_url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space ID:{self.id}, Name:{self.name}, Description:{self.description}, Price:{self.price}, Picture URL:{self.picture_url}"