from flask_app.common.BaseModel import BaseModel
from flask_app.extensions import db


class Author(BaseModel):
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    books = db.relationship("Book", backref="author", lazy=True, cascade="all, delete-orphan")

    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return f"<Author: {self.first_name} {self.last_name}>"
