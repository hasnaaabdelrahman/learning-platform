from app import db

class Enrollment(db.Model):

    __tablename__ = "enrollment"

    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer , db.ForeignKey("user.id")  , nullable = False)
    course_id = db.Column(db.Integer , db.ForeignKey("course.id") , nullable = False)