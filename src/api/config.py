class Config(object):
    DEBUG = False
    CSRF_ENABLED = True


class DevelopementConfig(Config):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "postgresql://jeremiah-ang:\
        @localhost:5432/examtt"
