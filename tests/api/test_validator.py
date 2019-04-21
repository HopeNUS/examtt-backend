import src.api.validator as validator
import json
import unittest


class Test_validator(unittest.TestCase):
    def test_AddExamValid(self):
        jsonObj = json.loads('''{
            "name": "name",
            "lifegroup": "lifegroup",
            "modules": [
                {
                    "code": "code",
                    "date": "01",
                    "month": "MMM",
                    "hour": "02",
                    "minute": "03",
                    "location": "location"
                }
            ]
        }''')
        self.assertTrue(
            validator
            .validateAddPrayerWarriorSubscriptionJson(jsonObj))

    def test_AddExamNoName(self):
        jsonObj = json.loads('''{
            "lifegroup": "lifegroup",
            "modules": [
                {
                    "code": "code",
                    "date": "12",
                    "month": "MMM",
                    "hour": "02",
                    "minute": "03",
                    "location": "location"
                }
            ]
        }''')
        self.assertFalse(
            validator
            .validateAddPrayerWarriorSubscriptionJson(jsonObj))

    def test_AddExamInvalidDate(self):
        # date is supposed to be 2 character exactly
        jsonObj = json.loads('''{
            "name": "name",
            "lifegroup": "lifegroup",
            "modules": [
                {
                    "code": "code",
                    "date": "2",
                    "month": "MMM",
                    "hour": "02",
                    "minute": "03",
                    "location": "location"
                }
            ]
        }''')
        self.assertFalse(
            validator
            .validateAddPrayerWarriorSubscriptionJson(jsonObj))

    def test_AddExamInvalidHour(self):
        # hour should be string not numeric
        jsonObj = json.loads('''{
            "name": "name",
            "lifegroup": "lifegroup",
            "modules": [
                {
                    "code": "code",
                    "date": "2",
                    "month": "MMM",
                    "hour": 12,
                    "minute": "03",
                    "location": "location"
                }
            ]
        }''')
        self.assertFalse(
            validator
            .validateAddPrayerWarriorSubscriptionJson(jsonObj))

    def test_AddExamInvalidMonth(self):
        # month is supposed to be 3 letter only
        jsonObj = json.loads('''{
            "name": "name",
            "lifegroup": "lifegroup",
            "modules": [
                {
                    "code": "code",
                    "date": "01",
                    "month": "MMMMMM",
                    "hour": "02",
                    "minute": "03",
                    "location": "location"
                }
            ]
        }''')
        self.assertFalse(
            validator
            .validateAddPrayerWarriorSubscriptionJson(jsonObj))

    def test_AddExamInvalidTime(self):
        # hour is supposed to be 2 letter only
        jsonObj = json.loads('''{
            "name": "name",
            "lifegroup": "lifegroup",
            "modules": [
                {
                    "code": "code",
                    "date": "01",
                    "month": "MMMMMM",
                    "hour": "103",
                    "minute": "03",
                    "location": "location"
                }
            ]
        }''')
        self.assertFalse(
            validator
            .validateAddPrayerWarriorSubscriptionJson(jsonObj))

    def test_AddPrayerWarriorValid(self):
        jsonObj = json.loads('''{
            "warrior": "warrior",
            "prayerSlot": [1,2,3]
        }''')
        self.assertTrue(
            validator
            .validateAddPrayerWarriorSubscriptionJson(jsonObj))
    
    def test_AddPrayerWarriorInvalidNumbers(self):
        # prayerSlot should be numeric
        jsonObj = json.loads('''{
            "warrior": "warrior",
            "prayerSlot": [1,"1"]
        }''')
        self.assertFalse(
            validator
            .validateAddPrayerWarriorSubscriptionJson(jsonObj))

    def test_DeletePrayerWarriorValid(self):
        jsonObj = json.loads('''{
            "prayerSlotWarriors": [
                {
                    "warriorName": "warriorName",
                    "prayerSlot": 1
                },
                {
                    "warriorName": "warriorName",
                    "prayerSlot": 2
                }
            ]
        }''')
        self.assertTrue(
            validator
            .validateAddPrayerWarriorSubscriptionJson(jsonObj))

    def test_DeletePrayerWarriorInvalidKeyName(self):
        # prayerSlotWarrior instead of prayerSlotWarriors
        jsonObj = json.loads('''{
            "prayerSlotWarrior": [
                {
                    "warriorName": "warriorName",
                    "prayerSlot": 1
                }
            ]
        }''')
        self.assertFalse(
            validator
            .validateAddPrayerWarriorSubscriptionJson(jsonObj))
