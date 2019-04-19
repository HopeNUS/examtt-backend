import json


class StudentExamTimetable(object):
    exams = []
    studentsMap = {}

    def addExam(self, id, code, time, date, location, meetingPoint):
        self.exams.append({
            'id': id,
            'code': code,
            'date': date,
            'time': time,
            'location': location,
            'meetingPoint': meetingPoint})

    def addStudent(self, name, lifegroup, module):
        if name not in self.studentsMap:
            self.studentsMap[name] = {'lifegroup': lifegroup, 'module': []}
        self.studentsMap[name]['module'].append(module)

    def serialise(self):
        students = []
        for name, info in self.studentsMap.items():
            students.append({
                'name': name,
                'lifegroup': info['lifegroup'],
                'module': info['module']})

        return json.dumps(
            {'exams': self.exams, 'students': students},
            sort_keys=True, indent=4)
