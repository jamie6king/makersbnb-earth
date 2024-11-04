class User:
    def __init__(self, id, name, email, phone_number, password):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.email}, {self.phone_number})"
    
    