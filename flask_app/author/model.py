from flask_app.extensions import db
from datetime import datetime


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.Date(), nullable=False, default=datetime.utcnow)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    books = db.relationship("Book", backref="author", lazy=True, cascade="all, delete-orphan")

    def __int__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return f"<Author: {self.first_name} {self.last_name}>"
