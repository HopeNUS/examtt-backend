from .logicController import LogicController


class StudentLogicController(LogicController):

    def getLifegroups(self):
        '''
        Fetches and returns the list of lifegroups
        '''
        return [lifegroup.name for lifegroup in self.getDb().getLifegroup()]

    def addStudentExamSchedule(self, addStudentExamScheduleJson):
        '''
        Populates database with the given schedule information
        Returns true if successful, false otherwise
        '''
        pass
