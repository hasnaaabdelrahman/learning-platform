from extensions import db

class Course(db.Model):

    __tablename__ = "course"


    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text , nullable=False)
    price = db.Column(db.Float, nullable=False)
    total_hours = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    enrollments = db.relationship("Enrollment" , backref = "course")
    comments = db.relationship("Comment" , backref = "course")


    def __init__(self , title , description , price , total_hours , rating):
        self.title = title
        self.description = description
        self.price = price
        self.total_hours = total_hours
        self.rating = rating

    def __repr__(self):
        return f"<Course -> title: {self.title}, description: {self.description}>"