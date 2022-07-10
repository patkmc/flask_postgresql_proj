import flask_app.book.model as m


class BookDto:
    def __init__(self, book_id: int, title: str, genre: str, release_date: str) -> None:
        self.id = book_id
        self.title = title
        self.genre = genre
        self.release_date = release_date


def to_dto(book: m.Book) -> BookDto:
    return BookDto(book.id, book.title, book.genre, str(book.release_date))
