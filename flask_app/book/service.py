from flask_app.book.dto import BookDto
from flask_app.book.dto import to_dto
from flask_app.book.model import Book
from flask_app.common.utils import transactional
from flask_app.extensions import db
from flask_app.tag.service import get_by_ids as get_tags_by_ids


def get_all() -> [BookDto]:
    books = Book.query.all()
    return [to_dto(b) for b in books]


def get_by_id(book_id: int) -> BookDto:
    return to_dto(_get_by_id(book_id))


@transactional
def add(book_data: dict) -> BookDto:
    new_book = Book(
        title=book_data["title"],
        genre=book_data["genre"],
        release_date=book_data["release_date"],
        author_id=book_data["author_id"],
    )
    db.session.add(new_book)
    return to_dto(new_book)


@transactional
def update(book_data: dict) -> BookDto:
    book = _get_by_id(book_data["id"])
    book.title = book_data["title"]
    book.genre = book_data["genre"]
    book.release_date = book_data["release_date"]

    if book_data["tags"]:
        book.tags = get_tags_by_ids([t.get("id") for t in book_data["tags"]])

    db.session.add(book)
    return to_dto(book)


@transactional
def delete(book_id: int) -> None:
    db.session.delete(_get_by_id(book_id))


def _get_by_id(book_id: int) -> Book:
    return Book.query.get_or_404(book_id)
