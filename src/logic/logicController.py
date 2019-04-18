from ..database.databaseController import DatabaseController


class LogicController(object):
    def __init__(self, db):
        self.dbController = DatabaseController(db)

    def getDb(self):
        return self.dbController
