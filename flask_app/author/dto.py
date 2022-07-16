from dataclasses import dataclass

import flask_app.author.model as m
import flask_app.book.dto as book_dto


@dataclass(frozen=True, kw_only=True)
class AuthorDetailsDto:
    birth_date: str
    birth_place: str
    bio: str


@dataclass(frozen=True, kw_only=True)
class AuthorDto:
    id: int
    first_name: str
    last_name: str
    books: [book_dto.BookDto]
    author_details: AuthorDetailsDto


def to_dto(author: m.Author) -> AuthorDto:
    return AuthorDto(
        id=author.id,
        first_name=author.first_name,
        last_name=author.last_name,
        books=[book_dto.to_dto(b) for b in author.books],
        author_details=_author_details_to_dto(author.author_details),
    )


def _author_details_to_dto(author_details: m.AuthorDetails):
    if author_details:
        return AuthorDetailsDto(
            birth_date=str(author_details.birth_date),
            birth_place=author_details.birth_place,
            bio=author_details.bio,
        )
    return None
