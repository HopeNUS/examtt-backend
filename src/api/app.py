from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from ..logic.locationLogicController import LocationLogicController
from ..logic.studentLogicController import StudentLogicController
from ..logic.warriorLogicController import WarriorLogicController

locationLogicController = LocationLogicController(db)
studentLogicController = StudentLogicController(db)
warriorLogicController = WarriorLogicController(db)


@app.route("/")
def home():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
