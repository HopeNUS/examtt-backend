import unittest
import json
from src.api import app


class Test_StudentLogicController(unittest.TestCase):
    def test_getStudentExamTimetable(self):
        expected = json.loads('''{
                "exams": [
                    {
                        "code": "unittest",
                        "date": "01JAN",
                        "id": 3,
                        "location": "unittest",
                        "meetingPoint": null,
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
                        "module": ["integration1", "integration2"],
                        "name": "integration1"
                    },
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
        self.assertEqual(sorted(actual.items()), sorted(expected.items()))

    def test_getPrayerSlotTimetable(self):
        expected = json.loads('''{
            "prayerSlots": [
                {
                    "date": "01JAN",
                    "id": 2,
                    "location": "unittest",
                    "meetingPoint": null,
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
            "prayerSlotsWarriors": []
        }''')
        actual = json.loads(
            app
            .warriorLogicController.getPrayerSlotTimeTable("01", "JAN")
            .serialise())
        self.assertEqual(sorted(actual.items()), sorted(expected.items()))


if __name__ == '__main__':
    unittest.main()
