import unittest
from src.api import app
from src.exceptions.foreignKeyException import ForeignKeyException
from src.exceptions.uniqueException import UniqueException

app.app.app_context().push()


class Test_DatebaseController(unittest.TestCase):
    dbCtrl = app.studentLogicController.getDb()

    def test_addExamValid(self):
        moduleCode = "unittest"
        day = "01"
        month = "JAN"
        hour = "00"
        minute = "00"
        loc = "unittest"
        studentName = "unittest"
        lifegroup = "Others"
        self.dbCtrl.deleteStudentRecord(studentName)
        self.assertTrue(
            self.dbCtrl.addExam(
                studentName, lifegroup, moduleCode,
                day, month, hour, minute, loc)
            )

        moduleCode = "unittest2"
        day = "01"
        month = "JAN"
        hour = "00"
        minute = "00"
        loc = "unittest2"
        studentName = "unittest2"
        lifegroup = "Others"
        self.dbCtrl.deleteStudentRecord(studentName)
        self.assertTrue(
            self.dbCtrl.addExam(
                studentName, lifegroup, moduleCode,
                day, month, hour, minute, loc)
            )

        moduleCode = "unittest3"
        day = "01"
        month = "JAN"
        hour = "02"
        minute = "00"
        loc = "unittest3"
        studentName = "unittest"
        lifegroup = "Others"
        self.assertTrue(
            self.dbCtrl.addExam(
                studentName, lifegroup, moduleCode,
                day, month, hour, minute, loc)
            )

        moduleCode = "unittest3"
        day = "02"
        month = "JAN"
        hour = "02"
        minute = "00"
        loc = "unittest3"
        studentName = "unittest"
        lifegroup = "Others"
        self.assertRaises(
            UniqueException,
            self.dbCtrl.addExam,
            studentName, lifegroup, moduleCode,
            day, month, hour, minute, loc)

    def test_addExamInvalidLifegroup(self):
        self.assertRaises(
            ForeignKeyException,
            self.dbCtrl.addExam,
            "name", "Invalid", "", "", "", "", "", "")

    def test_retrieveExam(self):
        self.assertTrue(self.dbCtrl.getExamTimetable("01", "JAN"))
        self.assertFalse(self.dbCtrl.getExamTimetable("11", "JAN"))

    def test_retrievePrayerSlot(self):
        self.assertTrue(self.dbCtrl.getPrayerSlotTimeTable("01", "JAN"))
        self.assertTrue(self.dbCtrl.getPrayerSlotTimeTable(
            "01", "JAN", time=("02", "00")))
        self.assertFalse(self.dbCtrl.getPrayerSlotTimeTable("11", "JAN"))
        self.assertTrue(self.dbCtrl.getPrayerSlotTimeTable(
            "01", "JAN", ("00", "00"), "unittest"))

    def test_retrieveStudentsModule(self):
        self.assertTrue(self.dbCtrl.getStudentsModule())

    def test_addPrayerWarriorSubscription(self):
        self.assertTrue(
            self.dbCtrl.addPrayerWarriorSubscription("unittestW", 2))
        self.assertRaises(
            ForeignKeyException,
            self.dbCtrl.addPrayerWarriorSubscription,
            "unittestW", 9999,)

    def test_deletePrayerWarriorSubscription(self):
        self.assertTrue(
            self.dbCtrl.addPrayerWarriorSubscription("unittestDel", 2))
        self.assertTrue(
            self.dbCtrl.deletePrayerWarriorSubscription(2, "unittestDel"))


if __name__ == '__main__':
    unittest.main()
