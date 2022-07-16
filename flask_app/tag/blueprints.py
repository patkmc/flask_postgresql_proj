from flask import Blueprint
from flask import request
from flask_app.common.utils import to_json
from flask_app.tag import service

bp = Blueprint("tag", __name__, url_prefix="/tag")


@bp.get("/")
def get_all():
    return to_json(service.get_all()), 200


@bp.get("/<int:tag_id>")
def get_by_id(tag_id: int):
    return to_json(service.get_by_id(tag_id)), 200


@bp.post("/")
def add():
    if request.is_json:
        tag_data = request.get_json()
        return to_json(service.add(tag_data)), 200
    return {"error": "The request payload is not in JSON format"}, 500


@bp.put("/")
def update():
    if request.is_json:
        tag_data = service.update(request.get_json())
        return to_json(tag_data), 200
    return {"error": "The request payload is not in JSON format"}, 500


@bp.delete("/<int:tag_id>")
def delete(tag_id: int):
    service.delete(tag_id)
    return {"message": f"Tag with ID {tag_id} has been successfully deleted"}, 200
