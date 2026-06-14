import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from extensions import db, migrate
import models


app = Flask(__name__)

## configurations ##

app.config.from_object("config")

db.init_app(app)
migrate.init_app(app , db)



@app.route("/")
def sayHello():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)