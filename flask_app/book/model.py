from flask_app.common.BaseModel import BaseModel
from flask_app.extensions import db


class Book(BaseModel):
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date())
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)

    def __init__(self, title, genre, release_date, author_id):
        super().__init__()
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.author_id = author_id

    def __repr__(self):
        return f"<Book {self.title}>"
