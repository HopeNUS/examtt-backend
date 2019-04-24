from sqlalchemy import exc
from psycopg2.errors import UniqueViolation
from ..data.locationMeetingPoint import LocationMeetingPoint
from .model.lifegroup import Lifegroup
from .model.student import Student
from .model.module import Module
from .model.studentExam import StudentExam
from .model.date import Date
from .model.time import Time
from .model.dateTime import DateTime
from .model.meetingPoint import MeetingPoint
from .model.location import Location
from .model.warrior import Warrior
from .model.prayerSlot import PrayerSlot
from .model.prayerSlotWarrior import PrayerSlotWarrior
from .model.exam import Exam
from ..exceptions.foreignKeyException import ForeignKeyException
from ..exceptions.uniqueException import UniqueException


class DatabaseController(object):
    def __init__(self, Session):
        self.Session = Session

    def startSession(self):
        return self.Session()

    def closeSession(self, session):
        session.close()

    def deleteRecord(self, session, model, **kwargs):
        entity = model.query.filter_by(**kwargs).first()
        if not entity:
            return
        entity = session.merge(entity)
        session.delete(entity)
        session.flush()

    def deleteStudentRecord(self, studentName):
        session = self.startSession()
        self.deleteRecord(session, Student, name=studentName)
        self.closeSession(session)

    def getOrCreate(self, session, model, **kwargs):
        instance = session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance, False

        try:
            instance = model(**kwargs)
            session.add(instance)
            session.flush()
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

        session = self.startSession()
        self.getOrCreate(
            session, Student, name=studentName, lifegroup=lifegroup)
        self.getOrCreate(
            session, Module, code=moduleCode)
        self.getOrCreate(
            session, Date, date=day, month=month)
        self.getOrCreate(
            session, Time, hour=hour, minute=minute)
        dateTime, _ = self.getOrCreate(
            session, DateTime, dateDate=day, dateMonth=month,
            timeHour=hour, timeMinute=minute)
        self.getOrCreate(
            session, Location, name=location)
        prayerSlot, _ = self.getOrCreate(
            session, PrayerSlot,
            locationName=location, dateTimeId=dateTime.id)
        exam, _ = self.getOrCreate(
            session, Exam,
            moduleCode=moduleCode, prayerSlotId=prayerSlot.id)
        print(exam)
        self.getOrCreate(
            session, StudentExam,
            studentName=studentName, examId=exam.id)
        session.commit()
        self.closeSession(session)
        return True

    def addPrayerWarriorSubscription(self, warriorName, prayerSlot):
        '''
        Adds prayer warrior subscription

        Post requirement:
            Entries in database:
                a PrayerSlotWarrior entry <warriorName, prayerSlot>
        '''
        session = self.startSession()
        self.getOrCreate(session, Warrior, name=warriorName)
        self.getOrCreate(
            session,
            PrayerSlotWarrior,
            prayerSlotId=prayerSlot, warriorName=warriorName)
        session.commit()
        self.closeSession(session)
        return True

    def deletePrayerWarriorSubscription(self, prayerSlotId, warriorName):
        '''
        Adds prayer warrior subscription

        Post requirement:
            Entries in database:
                a no entry with <prayerSlotId, warriorName>
        '''
        session = self.startSession()
        self.deleteRecord(
            session,
            PrayerSlotWarrior,
            prayerSlotId=prayerSlotId, warriorName=warriorName)
        session.commit()
        self.closeSession(session)
        return True

    def setLocationMeetingPoint(self, location, meetingPoint):
        '''
        Adds prayer warrior subscription

        Post requirement:
            Entries in database:
                Location entry with name <location> has
                    meeting_point entry as <meetingPoint>
        '''
        session = self.startSession()
        locationEntity = self.getOrCreate(
            session, Location, name=location)
        locationEntity.meetingPointName = meetingPoint
        session.commit()
        self.closeSession(session)
        return True

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
            prayerSlotId: prayerSlotId
        }, ]

        No changes made to database
        '''
        session = self.startSession()
        dateTimeIdx = 0
        prayerSlotIdx = 1
        locationIdx = 2
        examIdx = 3
        result = [{
            'id': exam[examIdx].id,
            'code': exam[examIdx].moduleCode,
            'hour': exam[dateTimeIdx].timeHour,
            'minute': exam[dateTimeIdx].timeMinute,
            'date': exam[dateTimeIdx].dateDate,
            'month': exam[dateTimeIdx].dateMonth,
            'location': exam[prayerSlotIdx].locationName,
            'meetingPoint': exam[locationIdx].meetingPointName,
            'prayerSlotId': exam[prayerSlotIdx].id}
            for exam in session.query(
                DateTime, PrayerSlot, Location, Exam)
            .filter_by(dateDate=date, dateMonth=month)
            .join(PrayerSlot, PrayerSlot.dateTimeId == DateTime.id)
            .join(Location, PrayerSlot.locationName == Location.name)
            .join(Exam, Exam.prayerSlotId == PrayerSlot.id)
            .all()]
        self.closeSession(session)
        return result

    def getStudentsModule(self, date=None, time=None, location=None):
        '''
        @param date = (date, month)
        @param time = (hour, minute)
        @param location = location

        Fetch and Returns
        [{
            name: studentName,
            lifegroup: lifegroup,
            module: module,
        }, ]

        No changes made to database
        '''
        session = self.startSession()
        studentIdx = 0
        examIdx = 1

        query = session.query(Student, Exam)\
            .join(StudentExam, Student.name == StudentExam.studentName)
        query = query\
            .join(Exam, Exam.id == StudentExam.examId)\
            .join(PrayerSlot, Exam.prayerSlotId == PrayerSlot.id)
        if location:
            query = query.filter_by(locationName=location)
        query = query.join(DateTime, PrayerSlot.dateTimeId == DateTime.id)
        if date:
            query = query.filter_by(dateDate=date[0], dateMonth=date[1])
        if time:
            query = query.filter_by(timeHour=time[0], timeMinute=time[1])

        result = [{
            'name': studentModule[studentIdx].name,
            'lifegroup': studentModule[studentIdx].lifegroup,
            'examId': studentModule[examIdx].id,
            'module': studentModule[examIdx].moduleCode}
            for studentModule in query.all()]
        self.closeSession(session)
        return result

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
        session = self.startSession()

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

        query = session\
            .query(DateTime, PrayerSlot, Location)\
            .filter_by(**filters)\
            .join(PrayerSlot, PrayerSlot.dateTimeId == DateTime.id)\
            .join(Location, PrayerSlot.locationName == Location.name)\

        if meetingPoint:
            query = query.filter(Location.name == meetingPoint)

        print(query)

        result = [{
            'id': prayerSlot[prayerSlotIdx].id,
            'hour': prayerSlot[dateTimeIdx].timeHour,
            'minute': prayerSlot[dateTimeIdx].timeMinute,
            'date': prayerSlot[dateTimeIdx].dateDate,
            'month': prayerSlot[dateTimeIdx].dateMonth,
            'location': prayerSlot[prayerSlotIdx].locationName,
            'meetingPoint': prayerSlot[locationIdx].meetingPointName}
            for prayerSlot in query.all()]
        self.closeSession(session)
        return result

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

    def getPrayerSlotsWarriors(self, date=None, time=None, location=None):
        '''
        @param date = (date, month)
        @param time = (hour, minute)
        @param location = location

        Fetches and returns the list of prayer slot and warriors

        returns [{
            prayerSlot: prayerSlotId,
            warriorName: warriorName
        }]
        '''
        query = PrayerSlotWarrior\
            .query.order_by(PrayerSlotWarrior.prayerSlotId)\
            .join(PrayerSlot, PrayerSlotWarrior.prayerSlotId == PrayerSlot.id)\

        if location:
            query = query.filter_by(locationName=location)
        query = query.join(DateTime, PrayerSlot.dateTimeId == DateTime.id)

        if date:
            query = query.filter_by(dateDate=date[0], dateMonth=date[1])
        if time:
            query = query.filter_by(timeHour=time[0], timeMinute=time[1])

        return [{
            'prayerSlot': prayerSlotWarrior.prayerSlotId,
            'warriorName': prayerSlotWarrior.warriorName, }
            for prayerSlotWarrior in query.all()]
