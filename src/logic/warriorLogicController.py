from .logicController import LogicController


class WarriorLogicController(LogicController):

    def getExamTimeTable(self):
        '''
        Fetches and returns exam time table information from database
        '''
        return self.getDb().getExamTimetable().serialise()

    def getPrayerSlotTimeTable(self, date, meetingPoint=None):
        '''
        Fetches and returns prayer slot time table information
        based on the date and meeting point
        '''
        return self.getDb().getPrayerSlotTimeTable().serialise()

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
