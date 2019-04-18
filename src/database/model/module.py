from src.api.app import db


class Module(db.Model):
    __tablename__ = "module"

    code = db.Column(db.String(), primary_key=True)
    students = db.relationship('StudentModule', backref='module', lazy=True)

    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return '<Module: {}>'.format(self.code)

    def serialise(self):
        return {'code': self.code}
