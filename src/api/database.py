from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def makeSessionMaker(databaseURI):
    engine = create_engine(databaseURI, pool_size=15, max_overflow=0)
    Session = sessionmaker(bind=engine)
    return Session


db = SQLAlchemy()
