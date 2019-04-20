from src.api.database import db


class MeetingPoint(db.Model):
    __tablename__ = "meeting_point"

    name = db.Column(db.String(), primary_key=True)
    locations = db.relationship(
        'Location', backref='MeetingPoint',
        lazy=True, cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Meeting Point: {}>'.format(self.name)

    def serialise(self):
        return {'name': self.name}
