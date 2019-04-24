import json


class StudentExamTimetable(object):

    STUDENT_LIFEGROUP_KEY = 'lifegroup'
    STUDENT_EXAM_KEY = 'exam'
    STUDENT_NAME_KEY = 'name'

    def __init__(self):
        self.exams = []
        self.studentsMap = {}

    def addExam(self, id, code, time, date, location, meetingPoint):
        self.exams.append({
            'id': id,
            'code': code,
            'date': date,
            'time': time,
            'location': location,
            'meetingPoint': meetingPoint})

    def addStudent(self, name, lifegroup, exam):
        if name not in self.studentsMap:
            self.studentsMap[name] = {
                self.STUDENT_LIFEGROUP_KEY: lifegroup,
                self.STUDENT_EXAM_KEY: []}
        self.studentsMap[name][self.STUDENT_EXAM_KEY].append(exam)

    def serialise(self):
        students = []
        for name, info in self.studentsMap.items():
            students.append({
                self.STUDENT_NAME_KEY: name,
                self.STUDENT_LIFEGROUP_KEY: info[self.STUDENT_LIFEGROUP_KEY],
                self.STUDENT_EXAM_KEY: info[self.STUDENT_EXAM_KEY]})

        return json.dumps(
            {'exams': self.exams, 'students': students},
            sort_keys=True, indent=4)
