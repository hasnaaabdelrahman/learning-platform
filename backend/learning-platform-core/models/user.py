import uuid
from app import db



class User(db.Model):

    id = db.Column(db.Integer , primary_key = True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    password = db.Column(db.String(50))
    role = db.Column(db.String(10))

    def __init__(self , id , first_name , last_name , password , role):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.role = role

