from dataclasses import dataclass
from dataclasses import field

import flask_app.book.model as m
from flask_app.tag.dto import TagDto
from flask_app.tag.dto import to_dto as tag_to_dto


@dataclass(frozen=True, kw_only=True)
class BookDto:
    id: int
    title: str
    genre: str
    release_date: str
    tags: [TagDto] = field(default_factory=list)


def to_dto(book: m.Book) -> BookDto:
    return BookDto(
        id=book.id,
        title=book.title,
        genre=book.genre,
        release_date=str(book.release_date),
        tags=[tag_to_dto(t) for t in book.tags],
    )
