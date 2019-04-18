class StudentExamTimetable(object):
    students = []
    exams = []

    def addExam(self, id, code, time, date, location, meetingPoint):
        self.exams.append({id, code, date, time, location, meetingPoint})

    def addStudent(self, name, lifegroup, modules):
        self.students.append({name, lifegroup, modules})

    def serialise(self):
        return {self.exams, self.students}
