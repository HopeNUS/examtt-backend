from src.api.app import db


class Exam(db.Model):
    __tablename__ = "exam"

    id = db.Column(db.Integer, primary_key=True)
    moduleCode = db.Column(
        db.String(),
        db.ForeignKey('module.code', ondelete="CASCADE"),
        unique=True,
        nullable=False)
    prayerSlotId = db.Column(
        db.Integer,
        db.ForeignKey('prayer_slot.id', ondelete="CASCADE"),
        nullable=False)

    def __init__(self, moduleCode, prayerSlotId):
        self.moduleCode = moduleCode
        self.prayerSlotId = prayerSlotId

    def __repr__(self):
        return '<Exam: {}>'.format(self.id)

    def serialise(self):
        return {
            'id': self.id,
            'moduleCode': self.moduleCode,
            'prayerSlotId': self.prayerSlotId,
        }
