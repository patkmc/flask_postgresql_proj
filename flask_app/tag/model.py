from flask_app.common.BaseModel import BaseModel
from flask_app.extensions import db


class Tag(BaseModel):
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"<Tag {self.name}>"
