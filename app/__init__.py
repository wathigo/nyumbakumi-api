from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .api.v1 import version_one as v1

from instance.config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    print(config_name)
    app.register_blueprint(v1)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app

from app.utils.database.schemas import Person, Area, Ward, Constituency, County
