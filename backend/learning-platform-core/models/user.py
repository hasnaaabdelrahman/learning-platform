import uuid

class User:
    def __init__(self , id , first_name , last_name , password , role):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.role = role
