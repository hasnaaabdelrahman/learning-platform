import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

## configurations ##

app.config.from_object("config")



db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

@app.route("/")
def sayHello():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)