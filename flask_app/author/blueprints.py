from flask import Blueprint
from flask import request
from flask_app.author import service
from flask_app.common.utils import to_json

bp = Blueprint("author", __name__, url_prefix="/author")


@bp.get("/")
def get_all():
    return to_json(service.get_all()), 200


@bp.get("/<int:author_id>")
def get_by_id(author_id: int):
    return to_json(service.get_by_id(author_id)), 200


@bp.post("/")
def add():
    if request.is_json:
        new_author = service.add(request.get_json())
        return to_json(new_author), 200
    return {"error": "The request payload is not in JSON format"}, 500


@bp.put("/")
def update():
    if request.is_json:
        new_author = service.update(request.get_json())
        return to_json(new_author), 200
    return {"error": "The request payload is not in JSON format"}, 500


@bp.delete("/<int:author_id>")
def delete(author_id: int):
    service.delete(author_id)
    return {"message": f"Author with ID {author_id} has been successfully deleted"}, 200
