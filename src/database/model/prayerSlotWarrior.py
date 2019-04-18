from src.api.app import db


class PrayerSlotWarrior(db.Model):
    __tablename__ = "prayer_slot_warrior"

    id = db.Column(db.Integer, primary_key=True)
    prayerSlotId = db.Column(
        db.Integer,
        db.ForeignKey('prayer_slot.id', ondelete="CASCADE"),
        nullable=False)
    warriorName = db.Column(
        db.String(),
        db.ForeignKey('warrior.name', ondelete="CASCADE"),
        nullable=False)

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
