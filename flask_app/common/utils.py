import json

from flask import request
from flask_app.extensions import db


def transactional(func):
    def inner(*arg, **kwargs):
        with db.session.begin():
            returned_value = func(*arg, **kwargs)
            return returned_value

    return inner


def to_json(obj):
    return json.dumps(obj, default=lambda o: o.__dict__)


def fix_date_from_request(value: str):
    month = value["month"]
    day = value["day"]
    return f"{value['year']}-{'0' if month < 10 else ''}{month}-{'0' if day < 10 else ''}{day}"


def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj)

        return decorator

    return wrap
