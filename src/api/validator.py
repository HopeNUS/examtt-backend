def validateAddStudentExamScheduleJson(json):
    '''
    returns true if json is of valid format

    Valid Format:
        {
            "name": "name",
            "lifegroup": "lifegroup",
            "modules": [
                {
                    "code": "code",
                    "date": "dd",
                    "month": "MMM",
                    "hour": "hh",
                    "minute": "mm",
                    "location": "location",
                },
            ],
        }
    '''
    return False


def validateAddPrayerWarriorSubscriptionJson(json):
    '''
    returns true if json is of valid format

    Valid Format:
        {
            "warrior": "warrior",
            "prayerSlot": [prayerSlotId],
        }
    '''
    return False


def validateDeletePrayerWarriorSubscriptionJson(json):
    '''
    returns true if json is of valid format

    Valid Format:
        {
            "prayerSlotWarriors": [
                {
                    "warriorName": "warriorName",
                    "prayerSlot": prayerSlotId
                }
            ],
        }
    '''
    return False


def validateSetLocationMeetingPointJson(json):
    '''
    returns true if json is of valid format

    Valid Format:
        {
            "meetingPoints": [
                {
                    "meetingPoint": "meetingPoint",
                    "locations": [
                        "location",
                    ],
                },
            ],
        }
    '''
    return False
