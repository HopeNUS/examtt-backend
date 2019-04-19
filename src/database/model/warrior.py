from src.api.app import db


class Warrior(db.Model):
    __tablename__ = "warrior"

    name = db.Column(db.String(), primary_key=True)
    prayerSlots = db.relationship(
        'PrayerSlotWarrior', backref='warrior',
        lazy=True, cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Warrior: {}>'.format(self.name)

    def serialise(self):
        return {'warrior': self.name}
