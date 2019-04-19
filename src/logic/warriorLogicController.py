from .logicController import LogicController
from ..data.studentExamTimetable import StudentExamTimetable
from ..data.prayerSlotTimetable import PrayerSlotTimetable


class WarriorLogicController(LogicController):

    def getExamTimeTable(self, date, month):
        '''
        Fetches and returns exam time table information from database
        '''
        examTimetable = StudentExamTimetable()
        exams = self.getDb().getExamTimetable(date, month)
        for exam in exams:
            examTimetable.addExam(
                exam['id'],
                exam['code'],
                self.getTimeFormatted(exam['hour'], exam['minute']),
                self.getDateFormatted(exam['date'], exam['month']),
                exam['location'],
                exam['meetingPoint'])
        students = self.getDb().getStudentsModule()
        for student in students:
            examTimetable.addStudent(
                student['name'], student['lifegroup'], student['module'])
        return examTimetable

    def getPrayerSlotTimeTable(
            self, date, month, time=None, meetingPoint=None):
        '''
        Fetches and returns prayer slot time table information
        based on the date and meeting point
        '''
        prayerSlotTimetable = PrayerSlotTimetable()
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
        return prayerSlotTimetable

    def addPrayerWarriorSubscription(self, addPrayerWarriorSubscriptionJson):
        '''
        Populated database with the given subscription information
        Returns true if successful, false otherwise
        '''
        pass

    def deletePrayerWarriorSubscription(
            self, deletePrayerWarriorSubscriptionJson):
        '''
        Deletes entries in database based on the given subscription information
        Returns true if successful, false otherwise
        '''
        pass

    def getTimeFormatted(self, hour, minute):
        return "{}{}".format(hour, minute)

    def getDateFormatted(self, date, month):
        return "{}{}".format(date, month)
