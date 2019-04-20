from .logicController import LogicController
from ..exceptions.foreignKeyException import ForeignKeyException
from ..exceptions.uniqueException import UniqueException


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
        studentName = addStudentExamScheduleJson['name']
        self.getDb().deleteStudentRecord(studentName)
        lifegroup = addStudentExamScheduleJson['lifegroup']
        modules = addStudentExamScheduleJson['modules']
        failures = []
        successes = []
        for module in modules:
            code = module['code']
            date = module['date']
            month = module['month']
            hour = module['hour']
            minute = module['minute']
            location = module['location']
            try:
                self.getDb().addExam(
                    studentName, lifegroup, code, date,
                    month, hour, minute, location)
            except (ForeignKeyException, UniqueException) as e:
                failures.append((code, e))
            else:
                successes.append(code)

        return successes, failures
