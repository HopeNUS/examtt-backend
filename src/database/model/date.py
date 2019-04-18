from src.api.app import db


class Date(db.Model):
    __tablename__ = "date"

    date = db.Column(db.String(2), primary_key=True)
    month = db.Column(db.String(3), primary_key=True)
    dateTimes = db.relationship('DateTime', lazy=True)

    def __init__(self, date, month):
        self.date = date
        self.month = month

    def __repr__(self):
        return '<Date: {}{}>'.format(self.date, self.month)

    def serialise(self):
        return {'date': '{}{}'.format(self.date, self.month)}
