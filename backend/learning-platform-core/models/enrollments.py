import uuid

class Entrollment:

    id = db.Column(db.Integer , primary_key = True)
    
    def __init__(self , id):
        self.id