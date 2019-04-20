import unittest
from src.api import app

app.app.app_context().push()


class Test_StudentLogicController(unittest.TestCase):
    def test_getLifegroup(self):
        self.assertEqual(
            app.studentLogicController.getLifegroups(),
            [
                'A1', 'A2', 'A3',
                'B1', 'B2', 'B3',
                'C1', 'C2', 'C3',
                'D1', 'D2', 'D3',
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

        successes, failures = app.studentLogicController\
            .addStudentExamSchedule(addStudentExamScheduleJson)
        self.assertTrue(successes)
        self.assertFalse(failures)


if __name__ == '__main__':
    unittest.main()
