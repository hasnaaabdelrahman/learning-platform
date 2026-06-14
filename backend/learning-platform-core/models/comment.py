from extensions import db

class Comment(db.Model):

    __tablename__ = "comment"

    id = db.Column(db.Integer , primary_key = True)
    content = db.Column(db.Text , nullable = False)

    user_id = db.Column(db.Integer , db.ForeignKey("user.id") , nullable = False) 
    course_id = db.Column(db.Integer , db.ForeignKey("course.id") , nullable = False)

    def __init__(self ,content):
        self.content = content
        
    def __repr__(self):
        return f"<Comment {self.content}>"