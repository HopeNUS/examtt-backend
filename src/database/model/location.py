from src.api.database import db


class Location(db.Model):
    __tablename__ = "location"

    name = db.Column(db.String(), primary_key=True)
    meetingPointName = db.Column(
        db.String(),
        db.ForeignKey('meeting_point.name', ondelete="SET NULL"),
        nullable=True)

    prayerSlots = db.relationship(
        'PrayerSlot', backref='location',
        lazy=True, cascade="all, delete-orphan")

    def __init__(self, name, meetingPoint=None):
        self.name = name
        self.meetingPoint = meetingPoint

    def __repr__(self):
        return '<Location: {}>'.format(self.name)

    def serialise(self):
        return {'name': self.name}
