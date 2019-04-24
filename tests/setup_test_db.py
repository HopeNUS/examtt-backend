from flask import Flask
from src.api.config import TestConfig
from src.api.database import db, makeSessionMaker

config = TestConfig()
testApp = Flask(__name__)
print(config.SQLALCHEMY_DATABASE_URI)
Session = makeSessionMaker(config.SQLALCHEMY_DATABASE_URI)
testApp.config.from_object(config)
testApp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
testApp.app_context().push()
db.init_app(testApp)

from src.database.model.lifegroup import Lifegroup
from src.database.model.student import Student
from src.database.model.module import Module
from src.database.model.date import Date
from src.database.model.time import Time
from src.database.model.dateTime import DateTime
from src.database.model.meetingPoint import MeetingPoint
from src.database.model.location import Location
from src.database.model.warrior import Warrior
from src.database.model.prayerSlot import PrayerSlot
from src.database.model.prayerSlotWarrior import PrayerSlotWarrior
from src.database.model.exam import Exam
from src.database.model.studentExam import StudentExam


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    for lifegroupName in ["A1", "A2", "A3", "Others"]:
        lg = Lifegroup(lifegroupName)
        db.session.add(lg)
    db.session.commit()
