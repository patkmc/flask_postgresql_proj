from dataclasses import dataclass

import flask_app.tag.model as m


@dataclass(frozen=True, kw_only=True)
class TagDto:
    id: int
    name: str


def to_dto(tag: m.Tag) -> TagDto:
    return TagDto(id=tag.id, name=tag.name)
