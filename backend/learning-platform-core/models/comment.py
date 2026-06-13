import uuid

class Comment:

    id = db.Column(db.Integer , primary_key = True)
    content = db.Column(db.String(50))

    def __init__(self , id , content):
        self.id = str(uuid.uuid4())
        self.content = content
        