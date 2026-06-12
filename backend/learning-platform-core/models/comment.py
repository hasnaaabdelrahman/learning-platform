import uuid

class Comment:
    def __init__(self , id , content):
        self.id = str(uuid.uuid4())
        self.content = content
        