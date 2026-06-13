import bcrypt
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash

def hash_password_with_bcrypt(password):
    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password , salt)
    return hashed_password

def  hash_password(password):
    bcrypted = Bcrypt()
    hashed_password = bcrypted.generate_password_hash(password)
    return hashed_password

def hash_password_with_werkzeug(password):
    hashed_password = generate_password_hash(password)
    return hashed_password