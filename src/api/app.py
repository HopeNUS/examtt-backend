from flask import Flask
from .config import config
from .database import db, makeSessionMaker
from .routes import defineRoutes
from ..logic.locationLogicController import LocationLogicController
from ..logic.studentLogicController import StudentLogicController
from ..logic.warriorLogicController import WarriorLogicController


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app


app = create_app(config)
Session = makeSessionMaker(config.SQLALCHEMY_DATABASE_URI)
locationLogicController = LocationLogicController(Session)
studentLogicController = StudentLogicController(Session)
warriorLogicController = WarriorLogicController(Session)
defineRoutes(app, studentLogicController, warriorLogicController)

if __name__ == '__main__':
    app.run()
