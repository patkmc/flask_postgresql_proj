from datetime import datetime

from flask_app.extensions import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.Date(), nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date())
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __init__(self, title, genre, release_date, author_id):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.author_id = author_id

    def __repr__(self):
        return f"<Book {self.title}>"
