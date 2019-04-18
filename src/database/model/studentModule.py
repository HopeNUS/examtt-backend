from src.api.app import db


class StudentModule(db.Model):
    __tablename__ = "studentModule"

    id = db.Column(db.Integer, primary_key=True)
    studentName = db.Column(
        db.String(),
        db.ForeignKey('student.name', ondelete="CASCADE"),
        nullable=False)
    moduleCode = db.Column(
        db.String(),
        db.ForeignKey('module.code', ondelete="CASCADE"),
        nullable=False)

    def __init__(self, studentName, moduleCode):
        self.studentName = studentName
        self.moduleCode = moduleCode

    def __repr__(self):
        return '<StudentModule: {}>'.format(self.id)

    def serialise(self):
        return {
            'id': self.id,
            'studentName': self.studentName,
            'moduleCode': self.moduleCode,
        }
