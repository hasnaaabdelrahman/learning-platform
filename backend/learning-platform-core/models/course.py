import uuid
from app import db

class Course:

    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(200))
    price = db.Column(db.Double(50))
    total_hours = db.Column(db.Integer)
    rating = db.Column(db.Integer)


    def __init__(self , id , title , description , price , total_hours , rating):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.price = price
        self.total_hours = total_hours
        self.rating = rating