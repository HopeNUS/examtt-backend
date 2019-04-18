from .logicController import LogicController


class LocationLogicController(LogicController):

    def setLocationMeetingPoint(self, setLocationMeetingPointJson):
        '''
        Set meeting point of locations based on the given information
        Returns true if successful, false otherwise
        '''
        pass

    def getLocationsMeetingPoints(self):
        '''
        Fetches and returns the list of locations and the meeting points
        '''
        return self.getDb().getLocationsMeetingPoints().serialise()
