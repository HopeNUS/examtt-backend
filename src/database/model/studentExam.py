from src.api.database import db


class StudentExam(db.Model):
    __tablename__ = "studentExam"

    id = db.Column(db.Integer, primary_key=True)
    studentName = db.Column(
        db.String(),
        db.ForeignKey('student.name', ondelete="CASCADE"),
        nullable=False)
    examId = db.Column(
        db.Integer,
        db.ForeignKey('exam.id', ondelete="CASCADE"),
        nullable=False)

    def __init__(self, studentName, examId):
        self.studentName = studentName
        self.examId = examId

    def __repr__(self):
        return '<StudentModule: {}>'.format(self.id)

    def serialise(self):
        return {
            'id': self.id,
            'studentName': self.studentName,
            'examId': self.examId,
        }
