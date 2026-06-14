import os
from flask import Flask , request
from extensions import db, migrate,api
from config import DevConfig
from flask_restx import Resource , fields


app = Flask(__name__)

app.config.from_object(DevConfig)

api.init_app(app)
db.init_app(app)
migrate.init_app(app , db)

from routes.courses import *


if __name__ == "__main__":
    app.run(debug=True)