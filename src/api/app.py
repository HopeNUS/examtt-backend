import os
from flask import Flask
from .config import Config, DevelopementConfig
from .database import db
from .routes import defineRoutes
from ..logic.locationLogicController import LocationLogicController
from ..logic.studentLogicController import StudentLogicController
from ..logic.warriorLogicController import WarriorLogicController


def create_app():
    config = DevelopementConfig
    if os.environ.get('FLASK_ENV', "developement") == "production":
        config = Config

    app = Flask(__name__)
    app.config.from_object(config)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app


app = create_app()
locationLogicController = LocationLogicController(db)
studentLogicController = StudentLogicController(db)
warriorLogicController = WarriorLogicController(db)
defineRoutes(app, studentLogicController, warriorLogicController)

if __name__ == '__main__':
    app.run()
