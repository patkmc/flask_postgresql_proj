import logging
from logging import StreamHandler
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask_app.author import blueprints as book_bp
from flask_app.book import blueprints as author_bp
from flask_app.config import config_factory
from flask_app.extensions import db
from flask_app.extensions import migrate
from flask_app.tag import blueprints as tag_bp


def _configure_logging(flask_cfg):
    formatter = logging.Formatter("%(asctime)s: %(threadName)s : %(levelname)s: %(message)s")

    handlers = []
    # create logger with file handler
    file_logger = TimedRotatingFileHandler(f"{flask_cfg.LOG_FILE_PATH}/{flask_cfg.LOG_FILE_NAME}", when="midnight")
    file_logger.setLevel(flask_cfg.LOG_LEVEL)
    file_logger.setFormatter(formatter)
    handlers.append(file_logger)

    if flask_cfg.MODE == "development":
        handlers.append(StreamHandler())

    logging.basicConfig(level=flask_cfg.LOG_LEVEL, handlers=handlers)


def create_app(test_config=False):
    app = Flask(__name__)
    flask_cfg = config_factory(test_config)
    app.config.from_object(flask_cfg)
    _configure_logging(flask_cfg)
    db.init_app(app)
    migrate.init_app(app, db=db)

    for b in [author_bp, book_bp, tag_bp]:
        app.register_blueprint(b.bp)

    return app
