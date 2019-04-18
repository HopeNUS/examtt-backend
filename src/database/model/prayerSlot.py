from src.api.app import db


class PrayerSlot(db.Model):
    __tablename__ = "prayer_slot"

    id = db.Column(db.Integer, primary_key=True)
    locationName = db.Column(
        db.String(),
        db.ForeignKey('location.name', ondelete="CASCADE"),
        nullable=False)
    dateTimeId = db.Column(
        db.Integer,
        db.ForeignKey('date_time.id', ondelete="CASCADE"),
        nullable=False)
    warriors = db.relationship(
        'PrayerSlotWarrior', backref='prayer_slot', lazy=True)

    def __init__(self, locationName, dateTimeId):
        self.locationName = locationName
        self.dateTimeId = dateTimeId

    def __repr__(self):
        return '<PrayerSlot: {}>'.format(self.id)

    def serialise(self):
        return {
            'id': self.id,
            'locationName': self.locationName,
            'dateTimeId': self.dateTimeId,
        }
