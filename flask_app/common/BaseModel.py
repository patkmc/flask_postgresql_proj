from datetime import datetime

from flask_app.extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime(timezone=True), nullable=True)
