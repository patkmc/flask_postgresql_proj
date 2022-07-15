import json

from flask_app.extensions import db


def transactional(func):
    def inner(*arg, **kwargs):
        with db.session.begin():
            returned_value = func(*arg, **kwargs)
            return returned_value

    return inner


def to_json(obj):
    return json.dumps(obj, default=lambda o: o.__dict__)
