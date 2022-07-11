from flask import Flask
from flask_app.author import blueprints as book_bp
from flask_app.book import blueprints as author_bp
from flask_app.config import config_factory
from flask_app.extensions import db
from flask_app.extensions import migrate


def create_app(test_config=False):
    app = Flask(__name__)
    app.config.from_object(config_factory(test_config))
    db.init_app(app)
    migrate.init_app(app, db=db)

    for b in [author_bp, book_bp]:
        app.register_blueprint(b.bp)

    return app
