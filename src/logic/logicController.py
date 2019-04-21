from ..database.databaseController import DatabaseController


class LogicController(object):
    def __init__(self, Session):
        self.dbController = DatabaseController(Session)

    def getDb(self):
        return self.dbController
