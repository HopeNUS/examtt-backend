import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)


class DevelopementConfig(Config):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:\
        @localhost:5432/examtt"


class TestConfig(DevelopementConfig):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:\
        @localhost:5432/test_examtt"


config = DevelopementConfig
if os.environ.get('FLASK_ENV', "developement") == "production":
    config = Config
