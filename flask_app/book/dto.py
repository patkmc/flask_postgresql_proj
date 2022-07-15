from dataclasses import dataclass

import flask_app.book.model as m


@dataclass(frozen=True, kw_only=True)
class BookDto:
    book_id: int
    title: str
    genre: str
    release_date: str


def to_dto(book: m.Book) -> BookDto:
    return BookDto(
        book_id=book.id,
        title=book.title,
        genre=book.genre,
        release_date=str(book.release_date),
    )
