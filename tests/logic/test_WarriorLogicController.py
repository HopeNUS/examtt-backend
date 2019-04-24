import unittest
import json
from tests.setup_test_db import Session
from src.logic.warriorLogicController import WarriorLogicController

warriorLogicController = WarriorLogicController(Session)


class Test_StudentLogicController(unittest.TestCase):

    def test_getStudentExamTimetable(self):
        expected = json.loads('''{
                "exams": [
                    {
                        "code": "integration2",
                        "date": "03FEB",
                        "id": 6,
                        "location": "integration",
                        "meetingPoint": null,
                        "time": "0303"
                    }
                ],
                "students":
                [
                    {
                        "lifegroup": "Others",
                        "exam": [
                            6
                        ],
                        "name": "integration1"
                    }
                ]
            }''')
        actual = json.loads(
            warriorLogicController.getExamTimeTable("03", "FEB")
            .serialise())
        self.assertEqual(actual['exams'], expected['exams'])
        self.assertEqual(actual['students'], expected['students'])

    def test_getPrayerSlotTimetable(self):
        expected = json.loads('''{
            "prayerSlots": [
                {
                    "date": "02FEB",
                    "id": 5,
                    "location": "integration",
                    "meetingPoint": null,
                    "time": "0202"
                }
            ],
            "prayerSlotsWarriors": [
                [5, "integration1"]
            ]
        }''')
        actual = json.loads(
            warriorLogicController.getPrayerSlotTimeTable("02", "FEB")
            .serialise())
        self.assertEqual(sorted(actual.items()), sorted(expected.items()))

    def test_addAnddeletePrayerSlotWarrior(self):
        addObj = json.loads('''{
            "warrior": "integration1",
            "prayerSlot": [5,2,99,100]
        }''')
        expectedSuccesses = [5, 2]
        expectedFailures = [99, 100]
        successes, failures = warriorLogicController\
            .addPrayerWarriorSubscription(addObj)
        self.assertEqual(
            sorted(successes),
            sorted(expectedSuccesses))
        self.assertEqual(
            sorted(failures),
            sorted(expectedFailures))
        deleteObj = json.loads('''[
            {
                "warriorName": "integration1",
                "prayerSlot": 2
            },
            {
                "warriorName": "integration1",
                "prayerSlot": 1
            }
        ]''')
        self.assertTrue(
            warriorLogicController
            .deletePrayerWarriorSubscription(deleteObj))


if __name__ == '__main__':
    unittest.main()
