from flask_app.common.BaseModel import BaseModel
from flask_app.extensions import db


class Author(BaseModel):
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    books = db.relationship("Book", backref="author", lazy=True, cascade="all, delete-orphan")
    author_details = db.relationship("AuthorDetails", backref="author", uselist=False, cascade="all, delete-orphan")

    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return f"<Author: {self.first_name} {self.last_name}>"


class AuthorDetails(BaseModel):
    birth_date = db.Column(db.Date(), nullable=True)
    birth_place = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.String(4000), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))

    def __init__(self, birth_date=None, birth_place=None, bio=None):
        super().__init__()
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.bio = bio

    def __repr__(self) -> str:
        return (
            f"<Author details: \nDate of birth: {self.birth_date} \nPlace of birth: {self.birth_place} "
            f"\nBiography: {self.bio}>"
        )
