import unittest
from tests.setup_test_db import Session
from src.logic.studentLogicController import StudentLogicController

studentLogicController = StudentLogicController(Session)


class Test_StudentLogicController(unittest.TestCase):
    def test_getLifegroup(self):
        self.assertEqual(
            studentLogicController.getLifegroups(),
            [
                'A1', 'A2', 'A3',
                'Others']
            )

    def test_addStudentExamSchedule(self):
        addStudentExamScheduleJson = {
            'name': "integration1",
            'lifegroup': "Others",
            'modules': [
                {
                    'code': "integration1",
                    'date': '02',
                    'month': 'FEB',
                    'hour': '02',
                    'minute': '02',
                    'location': 'integration'
                },
                {
                    'code': "integration2",
                    'date': '03',
                    'month': 'FEB',
                    'hour': '03',
                    'minute': '03',
                    'location': 'integration'
                }
            ]
        }

        successes, failures = studentLogicController\
            .addStudentExamSchedule(addStudentExamScheduleJson)
        self.assertTrue(successes)
        self.assertFalse(failures)


if __name__ == '__main__':
    unittest.main()
