from src.api.app import db


class Time(db.Model):
    __tablename__ = "time"

    hour = db.Column(db.String(2), primary_key=True)
    minute = db.Column(db.String(2), primary_key=True)
    dateTimes = db.relationship(
        'DateTime', lazy=True, cascade="all, delete-orphan")

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return '<Time: {}{}>'.format(self.hour, self.minute)

    def serialise(self):
        return {'time': '{}{}'.format(self.hour, self.minute)}
