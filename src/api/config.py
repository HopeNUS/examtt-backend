import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)


class DevelopementConfig(Config):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "postgresql://jeremiah-ang:\
        @localhost:5432/examtt"
