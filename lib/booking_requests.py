class BookingRequests:
    def __init__(self, customer_id,start_date, end_date, space_id, owner_id, accepted):
        self.space_id= space_id
        self.start_date = start_date
        self.end_date= end_date
        self.owner_id = owner_id
        self.accepted = accepted
        self.customer_id = customer_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    

    def __repr__(self):
        return f"User ID:{self.id},customer_id:{self.customer_id} desired dates:{self.start_date}, to {self.end_date}, space:{self.space_id}, owner:{self.owner_id}, accepted:{self.accepted})"
        