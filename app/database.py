from pymongo import MongoClient
import mongomock

_client = None
_db = None

def init_db(uri, testing=False):
    global _client, _db

    if testing:
        _client = mongomock.MongoClient()
        _db = _client["testdb"]
    else:
        _client = MongoClient(uri)
        _db = _client.get_default_database()

def get_db():
    return _db