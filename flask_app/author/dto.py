from dataclasses import dataclass

import flask_app.author.model as m
import flask_app.book.dto as book_dto


@dataclass(frozen=True, kw_only=True)
class AuthorDto:
    author_id: int
    first_name: str
    last_name: str
    books: [book_dto.BookDto]


def to_dto(author: m.Author) -> AuthorDto:
    return AuthorDto(
        author_id=author.id,
        first_name=author.first_name,
        last_name=author.last_name,
        books=[book_dto.to_dto(b) for b in author.books],
    )
