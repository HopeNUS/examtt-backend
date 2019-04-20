from src.api.database import db


class PrayerSlotWarrior(db.Model):
    __tablename__ = "prayer_slot_warrior"

    prayerSlotId = db.Column(
        db.Integer,
        db.ForeignKey('prayer_slot.id', ondelete="CASCADE"),
        nullable=False, primary_key=True)
    warriorName = db.Column(
        db.String(),
        db.ForeignKey('warrior.name', ondelete="CASCADE"),
        nullable=False, primary_key=True)

    def __init__(self, prayerSlotId, warriorName):
        self.prayerSlotId = prayerSlotId
        self.warriorName = warriorName

    def __repr__(self):
        return '<PrayerSlotWarrior: {}>'.format(self.id)

    def serialise(self):
        return {
            'id': self.id,
            'prayerSlotId': self.prayerSlotId,
            'warriorName': self.warriorName,
        }
