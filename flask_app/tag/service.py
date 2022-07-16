from flask_app.common.utils import transactional
from flask_app.extensions import db
from flask_app.tag.dto import TagDto
from flask_app.tag.dto import to_dto
from flask_app.tag.model import Tag


def get_all() -> [TagDto]:
    tags = Tag.query.all()
    return [to_dto(b) for b in tags]


def get_by_id(tag_id: int) -> TagDto:
    return to_dto(_get_by_id(tag_id))


@transactional
def add(tag_data: dict) -> TagDto:
    new_tag = Tag(
        name=tag_data["name"],
    )
    db.session.add(new_tag)
    return to_dto(new_tag)


@transactional
def update(tag_data: dict) -> TagDto:
    tag = _get_by_id(tag_data["id"])
    tag.name = tag_data["name"]
    db.session.add(tag)
    return to_dto(tag)


@transactional
def delete(tag_id: int) -> None:
    db.session.delete(_get_by_id(tag_id))


def _get_by_id(tag_id: int) -> Tag:
    return Tag.query.get_or_404(tag_id)


def get_by_ids(tag_ids: [int]) -> [Tag]:
    return Tag.query.filter(Tag.id.in_(tag_ids)).all()
