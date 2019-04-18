from ..data.studentExamTimetable import StudentExamTimetable
from ..data.locationMeetingPoint import LocationMeetingPoint
from ..data.prayerSlotTimetable import PrayerSlotTimetable
from .model.lifegroup import Lifegroup
from .model.student import Student
from .model.module import Module
from .model.studentModule import StudentModule
from .model.date import Date
from .model.time import Time
from .model.dateTime import DateTime
from .model.location import Location
from .model.meetingPoint import MeetingPoint
from .model.warrior import Warrior
from .model.prayerSlot import PrayerSlot
from .model.prayerSlotWarrior import PrayerSlotWarrior
from .model.exam import Exam


class DatabaseController(object):
    def __init__(self, db):
        self.db = db

    def addExam(
            self, studentName, lifegroup,
            moduleCode, date, time, location):
        '''
        Adds exam schedule of a student

        Post requirement:
            Entries in database:
                a Student entry <studentName, lifegroup>
                a Module entry <moduleCode>
                a StudentModule entry <studentName, moduleCode>
                a Date entry <date>
                a Time entry <time>
                a DateTime entry <date, time>
                a Location entry <location>
                a PrayerSlot entry <location, dateTime>
                a Exam entry <moduleCode, prayerSlotId>
        '''
        pass

    def addPrayerWarriorSubscription(self, warriorName, prayerSlot):
        '''
        Adds prayer warrior subscription

        Post requirement:
            Entries in database:
                a PrayerSlotWarrior entry <warriorName, prayerSlot>
        '''
        pass

    def deletePrayerWarriorSubscription(self, prayerSlotWrriorId):
        '''
        Adds prayer warrior subscription

        Post requirement:
            Entries in database:
                a no entry with id <prayerSlotWrriorId>
        '''
        pass

    def setLocationMeetingPoint(self, location, meetingPoint):
        '''
        Adds prayer warrior subscription

        Post requirement:
            Entries in database:
                Location entry with name <location> has
                    meeting_point entry as <meetingPoint>
        '''
        pass

    def getExamTimetable(self):
        '''
        Fetch and Returns StudentExamTimetable
        with student and exams information filled up.

        No changes made to database
        '''
        studentExamTimetable = StudentExamTimetable()
        return studentExamTimetable

    def getPrayerSlotTimeTable(self, date, meetingPoint=None):
        '''
        Fetch and Returns PrayerSlotTimetable
        with prayer slot and warrior information filled up.

        Filters by date and meeting point if meeting point is not None

        No changes made to database
        '''
        prayerSlotTimetable = PrayerSlotTimetable()
        return prayerSlotTimetable

    def getLifegroup(self):
        '''
        Fetches and returns the list of lifegroups
        '''
        lifegroups = Lifegroup.query.order_by(Lifegroup.name).all()
        return lifegroups

    def getLocationsMeetingPoints(self):
        '''
        Fetch and Returns LocationMeetingPoint
        with location and meetingPoint information filled up.

        No changes made to database
        '''
        locationMeetingPoint = LocationMeetingPoint()
        return locationMeetingPoint
