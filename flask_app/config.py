import os


class Config:
    MODE = os.getenv("MODE")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")

    LOG_FILE_PATH = os.getenv("LOG_FILE_PATH")
    LOG_FILE_NAME = os.getenv("LOG_FILE_NAME")
    LOG_LEVEL = os.getenv("LOG_LEVEL")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

    ACCESS_CONTROL_ALLOW_ORIGIN = os.getenv("ACCESS_CONTROL_ALLOW_ORIGIN")


class TestConfig(Config):
    TESTING = True


def config_factory(test_config: bool) -> Config | TestConfig:
    if test_config:
        return TestConfig()
    return Config()
