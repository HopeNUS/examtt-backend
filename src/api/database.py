from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import config


def makeSessionMaker(databaseURI):
    engine = create_engine(databaseURI)
    Session = sessionmaker(bind=engine)
    return Session


db = SQLAlchemy()
