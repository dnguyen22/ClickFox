import pymongo


class DB(object):
    URI = "mongodb://127.0.0.1:27017"

    @staticmethod
    def init():
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client['clickfox_app']

    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)

    @staticmethod
    def insert_many(collection, data):
        DB.DATABASE[collection].insert_many(data)

    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)

    @staticmethod
    def find(collection, query, projection=None, limit=0):
        return DB.DATABASE[collection].find(query, projection=projection, limit=limit)
