import uuid


class Course:
    def __init__(self , id , title , description , price , total_hours , rating):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.total_hours = total_hours
        self.rating = rating