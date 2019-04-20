from src.api.database import db


class Student(db.Model):
    __tablename__ = "student"

    name = db.Column(db.String(), primary_key=True)
    lifegroup = db.Column(
        db.String(),
        db.ForeignKey('lifegroup.name', ondelete="SET NULL"),
        nullable=True)
    modules = db.relationship(
        'StudentModule',
        backref='student',
        lazy=True,
        cascade="all, delete-orphan")

    def __init__(self, name, lifegroup):
        self.name = name
        self.lifegroup = lifegroup

    def __repr__(self):
        return '<Student: {}>'.format(self.name)

    def serialise(self):
        return {
            'name': self.name,
            'lifegroup': self.lifegroup,
        }
