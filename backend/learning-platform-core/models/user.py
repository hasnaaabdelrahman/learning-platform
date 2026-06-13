from app import db
from services.password_service import hash_password

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer , primary_key = True)
    first_name = db.Column(db.String(10), nullable=False)
    last_name = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    enrollments = db.relationship("Enrollment" , backref = "user")
    comments = db.relationship("Comment" , backref = "user")


    def __init__(self , first_name , last_name , password , role):
        self.first_name = first_name
        self.last_name = last_name
        self.password = hash_password(password)
        self.role = role

    def __repr__(self):
        return f"<User => first name: {self.first_name}, last name: {self.last_name} has role: {self.role}>"

