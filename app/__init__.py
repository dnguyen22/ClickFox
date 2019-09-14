import os
import json
import datetime

from flask import Flask
from app.database import DB
from bson.objectid import ObjectId


class JSONEncoder(json.JSONEncoder):
    """ Extend json-encoder class """
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    DB.init()
    register_blueprints(app)
    app.json_encoder = JSONEncoder

    return app


def register_blueprints(app):
    from .calls import app as calls_blueprint
    app.register_blueprint(calls_blueprint)


if __name__ == "__main__":
    app = create_app()
