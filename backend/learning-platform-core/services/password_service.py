import bcrypt
from flask_bcrypt import Bcrypt


bcrypted = Bcrypt()

def  hash_password(password):
    hashed_password = bcrypted.generate_password_hash(password).decode('utf-8')
    return hashed_password

def check_password(hashed_password , password):
    bcrypt.check_password_hash(hashed_password , password)