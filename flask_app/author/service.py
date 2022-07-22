from flask_app.author.dto import AuthorDto
from flask_app.author.dto import to_dto
from flask_app.author.model import Author
from flask_app.author.model import AuthorDetails
from flask_app.book.model import Book
from flask_app.common.utils import fix_date_from_request
from flask_app.common.utils import transactional
from flask_app.extensions import db


def get_all() -> list[AuthorDto]:
    authors = Author.query.all()
    return [to_dto(a) for a in authors]


def get_by_id(author_id: int) -> AuthorDto:
    return to_dto(_get_by_id(author_id))


@transactional
def add(author_data: dict) -> AuthorDto:
    new_author = Author(first_name=author_data["first_name"], last_name=author_data["last_name"])
    if "books" in author_data and author_data["books"]:
        new_author.books = _add_new_book(new_author.id, author_data)

    if "author_details" in author_data:
        author_details = author_data["author_details"]
        new_author.author_details = AuthorDetails(
            birth_date=fix_date_from_request(author_details["birth_date"]),
            birth_place=author_details["birth_place"],
            bio=author_details["bio"],
        )
    else:
        new_author.author_details = AuthorDetails()

    db.session.add(new_author)
    return to_dto(new_author)


@transactional
def update(author_data: dict) -> AuthorDto:
    author = _get_by_id(author_data["id"])
    author.last_name = author_data["last_name"]
    author.first_name = author_data["first_name"]

    if "books" in author_data:
        books_ids_from_request = [int(nb["id"]) for nb in author_data["books"] if "id" in nb]
        books_ids_to_remove = [b.id for b in author.books if b.id not in books_ids_from_request]
        if books_ids_to_remove:
            _delete_books(books_ids_to_remove)

        author.books.extend(_add_new_book(author.id, author_data))

    if "author_details" in author_data:
        author_details = author.author_details
        new_author_details = author_data["author_details"]
        author_details.birth_date = fix_date_from_request(new_author_details["birth_date"])
        author_details.birth_place = new_author_details["birth_place"]
        author_details.bio = new_author_details["bio"]

    db.session.add(author)
    return to_dto(author)


@transactional
def delete(author_id: int) -> None:
    db.session.delete(_get_by_id(author_id))


def _get_by_id(author_id: int) -> Author:
    return Author.query.get_or_404(author_id)


def _add_new_book(author_id: int, author_data: dict) -> [Book]:
    new_books = []
    for book in author_data["books"]:
        if "id" not in book:
            new_book = Book(
                title=book["title"],
                genre=book["genre"],
                release_date=book["release_date"],
                author_id=author_id,
            )
            new_books.append(new_book)
    return new_books


def _delete_books(books_ids: [int]):
    for b in Book.query.filter(Book.id.in_(books_ids)).all():
        db.session.delete(b)
