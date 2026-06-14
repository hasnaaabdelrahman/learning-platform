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

from resources.courses import *
from resources.comments import *
from resources.users import *

api.add_namespace(course_ns)
api.add_namespace(comment_ns)
api.add_namespace(user_ns)


if __name__ == "__main__":
    app.run(debug=True)