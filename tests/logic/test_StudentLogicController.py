import unittest
from src.api import app


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


if __name__ == '__main__':
    unittest.main()
