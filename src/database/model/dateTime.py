from src.api.app import db


class DateTime(db.Model):
    __tablename__ = "date_time"

    id = db.Column(db.Integer, primary_key=True)
    dateDate = db.Column(
        db.String(2), nullable=False)
    dateMonth = db.Column(
        db.String(3), nullable=False)
    timeHour = db.Column(
        db.String(2), nullable=False)
    timeMinute = db.Column(
        db.String(2), nullable=False)
    __table_args__ = (db.ForeignKeyConstraint(
            ['dateDate', 'dateMonth'],
            ['date.date', 'date.month'],
            ondelete="CASCADE"
        ),
        db.ForeignKeyConstraint(
            ['timeHour', 'timeMinute'],
            ['time.hour', 'time.minute'],
            ondelete="CASCADE"
        ),
        {})
    prayerSlots = db.relationship(
        'PrayerSlot', backref='dateTime',
        lazy=True, cascade="all, delete-orphan")

    def __init__(self, dateDate, dateMonth, timeHour, timeMinute):
        self.dateDate = dateDate
        self.dateMonth = dateMonth
        self.timeHour = timeHour
        self.timeMinute = timeMinute

    def __repr__(self):
        return '<DateTime: {}{} - {}{}>'.format(
            self.dateDate, self.dateMonth, self.timeHour, self.timeMinute)

    def serialise(self):
        return {
            'id': self.id,
            'date': '{}{}'.format(self.dateDate, self.dateMonth),
            'time': '{}{}'.formate(self.timeHour, self.timeMinute),
        }
