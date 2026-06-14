import os
from flask import Flask
from flask_restx import Api , Resource
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from extensions import db, migrate
import models

from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)

api= Api(app,doc='/docs')


db.init_app(app)
migrate.init_app(app , db)



@api.route("/hello")
class HelloResource(Resource):
    def get(self):
        return {"message":"hello"}


if __name__ == "__main__":
    app.run(debug=True)