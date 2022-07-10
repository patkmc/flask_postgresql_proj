import flask_app.author.model as m
import flask_app.book.dto as book_dto


class AuthorDto:
    def __init__(self, author_id: int, first_name: str, last_name: str, books: [book_dto.BookDto]) -> None:
        self.id = author_id
        self.first_name = first_name
        self.last_name = last_name
        self.books = books


def to_dto(author: m.Author) -> AuthorDto:
    return AuthorDto(author.id, author.first_name, author.last_name, [book_dto.to_dto(b) for b in author.books])
