from src.api.app import db


class Lifegroup(db.Model):
    __tablename__ = "lifegroup"

    name = db.Column(db.String(), primary_key=True)
    students = db.relationship('Student', backref='lifegroupName', lazy=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Lifegroup: {}>'.format()

    def serialise(self):
        return {'lifegroup': self.name}
