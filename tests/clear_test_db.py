from .setup_test_db import testDb

if __name__ == "__main__":
    testDb.session.remove()
    testDb.drop_all()
