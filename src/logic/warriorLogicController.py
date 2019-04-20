from .logicController import LogicController
from ..data.studentExamTimetable import StudentExamTimetable
from ..data.prayerSlotTimetable import PrayerSlotTimetable
from ..exceptions.foreignKeyException import ForeignKeyException


class WarriorLogicController(LogicController):

    def getExamTimeTable(self, date, month):
        '''
        Fetches and returns exam time table information from database
        '''
        examTimetable = StudentExamTimetable()
        self.populateExamTimeTableExam(date, month, examTimetable)
        self.populateExamTimeTableStudent(date, month, examTimetable)
        return examTimetable

    def populateExamTimeTableStudent(self, date, month, examTimetable):
        students = self.getDb().getStudentsModule((date, month, ))
        for student in students:
            examTimetable.addStudent(
                student['name'], student['lifegroup'], student['module'])

    def populateExamTimeTableExam(self, date, month, examTimetable):
        exams = self.getDb().getExamTimetable(date, month)
        for exam in exams:
            examTimetable.addExam(
                exam['id'],
                exam['code'],
                self.getTimeFormatted(exam['hour'], exam['minute']),
                self.getDateFormatted(exam['date'], exam['month']),
                exam['location'],
                exam['meetingPoint'])

    def getPrayerSlotTimeTable(
            self, date, month, time=None, meetingPoint=None):
        '''
        Fetches and returns prayer slot time table information
        based on the date and meeting point
        '''
        prayerSlotTimetable = PrayerSlotTimetable()
        self.populatePrayerSlotTimetablePrayerSlot(
            date, month, time, meetingPoint, prayerSlotTimetable)
        self.populatePrayerSlotTimetableWarrior(
            date, month, time, meetingPoint, prayerSlotTimetable)
        return prayerSlotTimetable

    def populatePrayerSlotTimetableWarrior(
            self, date, month, time, meetingPoint, prayerSlotTimetable):
        prayerSlotsWarriors = self.getDb().getPrayerSlotsWarriors(
            (date, month), time, meetingPoint)
        for prayerSlotWarrior in prayerSlotsWarriors:
            prayerSlotTimetable.addPrayerSlotsWarrior(
                prayerSlotWarrior['prayerSlot'],
                prayerSlotWarrior['warriorName'])

    def populatePrayerSlotTimetablePrayerSlot(
            self, date, month, time, meetingPoint, prayerSlotTimetable):
        prayerSlots = self.getDb().getPrayerSlotTimeTable(
            date, month, time, meetingPoint)
        for prayerSlot in prayerSlots:
            prayerSlotTimetable.addPrayerSlot(
                prayerSlot['id'],
                prayerSlot['location'],
                prayerSlot['meetingPoint'],
                self.getDateFormatted(
                    prayerSlot['date'], prayerSlot['month']),
                self.getTimeFormatted(
                    prayerSlot['hour'], prayerSlot['minute']))

    def addPrayerWarriorSubscription(self, addPrayerWarriorSubscriptionJson):
        '''
        Populated database with the given subscription information
        Returns true if successful, false otherwise
        '''
        success = []
        failure = []
        warrior = addPrayerWarriorSubscriptionJson['warrior']
        for prayerSlot in addPrayerWarriorSubscriptionJson['prayerSlot']:
            try:
                self.getDb().addPrayerWarriorSubscription(
                    warrior, prayerSlot)
            except ForeignKeyException:
                failure.append(prayerSlot)
            else:
                success.append(prayerSlot)
        return success, failure

    def deletePrayerWarriorSubscription(
            self, deletePrayerWarriorSubscriptionJson):
        '''
        Deletes entries in database based on the given subscription information
        Returns true if successful, false otherwise
        '''
        for prayerSlotWarrior in deletePrayerWarriorSubscriptionJson:
            warriorName = prayerSlotWarrior['warriorName']
            prayerSlotId = prayerSlotWarrior['prayerSlot']
            self.getDb().deletePrayerWarriorSubscription(
                prayerSlotId, warriorName)
        return True

    def getTimeFormatted(self, hour, minute):
        return "{}{}".format(hour, minute)

    def getDateFormatted(self, date, month):
        return "{}{}".format(date, month)
