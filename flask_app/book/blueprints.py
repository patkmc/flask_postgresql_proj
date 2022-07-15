from flask import Blueprint
from flask import request
from flask_app.book import service
from flask_app.common.utils import to_json

bp = Blueprint("book", __name__, url_prefix="/book")


@bp.get("/")
def get_all():
    return to_json(service.get_all()), 200


@bp.get("/<int:book_id>")
def get_by_id(book_id: int):
    return to_json(service.get_by_id(book_id)), 200


@bp.post("/")
def add():
    if request.is_json:
        book_data = request.get_json()
        return to_json(service.add(book_data)), 200
    return {"error": "The request payload is not in JSON format"}, 500


@bp.put("/")
def update():
    if request.is_json:
        new_book = service.update(request.get_json())
        return to_json(new_book), 200
    return {"error": "The request payload is not in JSON format"}, 500


@bp.delete("/<int:book_id>")
def delete(book_id: int):
    service.delete(book_id)
    return {"message": f"Book with ID {book_id} has been successfully deleted"}, 200
