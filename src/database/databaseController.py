from sqlalchemy import exc
from psycopg2.errors import UniqueViolation
from ..data.locationMeetingPoint import LocationMeetingPoint
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
from ..exceptions.foreignKeyException import ForeignKeyException
from ..exceptions.uniqueException import UniqueException


class DatabaseController(object):
    def __init__(self, db):
        self.db = db

    def deleteStudentRecord(self, studentName):
        student = Student.query.filter_by(name=studentName).first()
        if student:
            self.db.session.delete(student)
        self.db.session.flush()

    def getOrCreate(self, model, **kwargs):
        instance = self.db.session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance, False

        try:
            instance = model(**kwargs)
            self.db.session.add(instance)
            self.db.session.flush()
        except exc.IntegrityError as e:
            if type(e.orig) is UniqueViolation:
                raise UniqueException(str(e))
            else:
                raise ForeignKeyException(str(e))

        return instance, True

    def addExam(
            self, studentName, lifegroup,
            moduleCode, day, month, hour, minute, location):
        '''
        Adds exam schedule of a student

        Post requirement:
            Entries in database:
                a Student entry <studentName, lifegroup>
                a Module entry <moduleCode>
                a StudentModule entry <studentName, moduleCode>
                a Date entry <day, month>
                a Time entry <hour, minute>
                a DateTime entry <day, month, hour, minute>
                a Location entry <location>
                a PrayerSlot entry <location, dateTime>
                a Exam entry <moduleCode, prayerSlotId>
        '''

        self.getOrCreate(
            Student, name=studentName, lifegroup=lifegroup)
        self.getOrCreate(
            Module, code=moduleCode)
        self.getOrCreate(
            StudentModule, studentName=studentName, moduleCode=moduleCode)
        self.getOrCreate(
            Date, date=day, month=month)
        self.getOrCreate(
            Time, hour=hour, minute=minute)
        dateTime, _ = self.getOrCreate(
            DateTime, dateDate=day, dateMonth=month,
            timeHour=hour, timeMinute=minute)
        self.getOrCreate(
            Location, name=location)
        prayerSlot, _ = self.getOrCreate(
            PrayerSlot, locationName=location, dateTimeId=dateTime.id)
        self.getOrCreate(
            Exam, moduleCode=moduleCode, prayerSlotId=prayerSlot.id)
        self.db.session.commit()

        return True

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

    def getExamTimetable(self, date, month):
        '''
        Fetch and Returns
        [{
            id: examId,
            code: moduleCode,
            hour: hour,
            minute: minute,
            date: date,
            month: month,
            location: location,
            meetingPoint: meetingPoint,
        }, ]

        No changes made to database
        '''
        dateTimeIdx = 0
        prayerSlotIdx = 1
        locationIdx = 2
        examIdx = 3
        return [{
            'id': exam[examIdx].id,
            'code': exam[examIdx].moduleCode,
            'hour': exam[dateTimeIdx].timeHour,
            'minute': exam[dateTimeIdx].timeMinute,
            'date': exam[dateTimeIdx].dateDate,
            'month': exam[dateTimeIdx].dateMonth,
            'location': exam[prayerSlotIdx].locationName,
            'meetingPoint': exam[locationIdx].meetingPointName}
            for exam in self.db.session.query(
                DateTime, PrayerSlot, Location, Exam)
            .filter_by(dateDate=date, dateMonth=month)
            .join(PrayerSlot, PrayerSlot.dateTimeId == DateTime.id)
            .join(Location, PrayerSlot.locationName == Location.name)
            .join(Exam, Exam.prayerSlotId == PrayerSlot.id)
            .all()]
    
    def getStudentsModule(self):
        '''
        Fetch and Returns
        [{
            name: studentName,
            lifegroup: lifegroup,
            module: module,
        }, ]

        No changes made to database
        '''
        studentIdx = 0
        studentModuleIdx = 1
        return [{
            'name': studentModule[studentIdx].name,
            'lifegroup': studentModule[studentIdx].lifegroup,
            'module': studentModule[studentModuleIdx].moduleCode}
            for studentModule in self.db.session.query(
                Student, StudentModule)
            .join(StudentModule, Student.name == StudentModule.studentName)
            .all()]

    def getPrayerSlotTimeTable(
            self, date, month, time=None, meetingPoint=None):
        '''
        @param time -- (hour, minute)

        Fetch and Returns
        [{
            id: prayerSlotId,
            hour: hour,
            minute: minute,
            date: date,
            month: month,
            meetingPoint: meetingPoint,
        }, ]

        No changes made to database
        '''
        dateTimeIdx = 0
        prayerSlotIdx = 1
        locationIdx = 2
        filters = {
            "dateDate": date,
            "dateMonth": month,
        }
        if time:
            filters['timeHour'] = time[0]
            filters['timeMinute'] = time[1]
        if meetingPoint:
            filters['meetingPoint'] = meetingPoint

        return [{
            'id': prayerSlot[prayerSlotIdx].id,
            'hour': prayerSlot[dateTimeIdx].timeHour,
            'minute': prayerSlot[dateTimeIdx].timeMinute,
            'date': prayerSlot[dateTimeIdx].dateDate,
            'month': prayerSlot[dateTimeIdx].dateMonth,
            'location': prayerSlot[prayerSlotIdx].locationName,
            'meetingPoint': prayerSlot[locationIdx].meetingPointName}
            for prayerSlot in self.db.session.query(
                DateTime, PrayerSlot, Location)
            .filter_by(**filters)
            .join(PrayerSlot, PrayerSlot.dateTimeId == DateTime.id)
            .join(Location, PrayerSlot.locationName == Location.name)
            .all()]

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
