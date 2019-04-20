import unittest
import json
from src.api import app

app.app.app_context().push()


class Test_StudentLogicController(unittest.TestCase):
    def test_getStudentExamTimetable(self):
        expected = json.loads('''{
                "exams": [
                    {
                        "code": "unittest",
                        "date": "01JAN",
                        "id": 3,
                        "location": "unittest",
                        "meetingPoint": "unittest",
                        "time": "0000"
                    },
                    {
                        "code": "unittest2",
                        "date": "01JAN",
                        "id": 4,
                        "location": "unittest2",
                        "meetingPoint": null,
                        "time": "0000"
                    },
                    {
                        "code": "unittest3",
                        "date": "01JAN",
                        "id": 5,
                        "location": "unittest3",
                        "meetingPoint": null,
                        "time": "0200"
                    }
                ],
                "students":
                [
                    {
                        "lifegroup": "Others",
                        "module": [
                            "unittest",
                            "unittest3"
                        ],
                        "name": "unittest"
                    },
                    {
                        "lifegroup": "Others",
                        "module": ["unittest2"],
                        "name": "unittest2"
                    }
                ]
            }''')
        actual = json.loads(
            app
            .warriorLogicController.getExamTimeTable("01", "JAN")
            .serialise())
        self.assertEqual(actual['exams'], expected['exams'])

    def test_getPrayerSlotTimetable(self):
        expected = json.loads('''{
            "prayerSlots": [
                {
                    "date": "01JAN",
                    "id": 2,
                    "location": "unittest",
                    "meetingPoint": "unittest",
                    "time": "0000"
                },
                {
                    "date": "01JAN",
                    "id": 5,
                    "location": "unittest2",
                    "meetingPoint": null,
                    "time": "0000"
                },
                {
                    "date": "01JAN",
                    "id": 6,
                    "location": "unittest3",
                    "meetingPoint": null,
                    "time": "0200"
                }
            ],
            "prayerSlotsWarriors": [
                [2, "unittestW"],
                [6, "unittest1"]
            ]
        }''')
        actual = json.loads(
            app
            .warriorLogicController.getPrayerSlotTimeTable("01", "JAN")
            .serialise())
        self.assertEqual(sorted(actual.items()), sorted(expected.items()))

    def test_addAnddeletePrayerSlotWarrior(self):
        addObj = json.loads('''{
            "warrior": "unittest1",
            "prayerSlot": [2,5,6]
        }''')
        expectedSuccesses = [2, 5, 6]
        successes, failures = app\
            .warriorLogicController\
            .addPrayerWarriorSubscription(addObj)
        self.assertEqual(
            sorted(successes),
            sorted(expectedSuccesses))
        self.assertFalse(failures)
        deleteObj = json.loads('''[
            {
                "warriorName": "unittest1",
                "prayerSlot": 2
            },
            {
                "warriorName": "unittest1",
                "prayerSlot": 5
            }
        ]''')
        self.assertTrue(
            app.warriorLogicController
            .deletePrayerWarriorSubscription(deleteObj))


if __name__ == '__main__':
    unittest.main()
