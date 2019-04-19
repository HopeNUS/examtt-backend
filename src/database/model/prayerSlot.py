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
    exams = db.relationship(
        'Exam', backref='prayerSlot', lazy=True, cascade="all, delete-orphan")
    warriors = db.relationship(
        'PrayerSlotWarrior', backref='prayerSlot',
        lazy=True, cascade="all, delete-orphan")

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
