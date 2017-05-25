import pymongo
from .input_base import InputPlugin


class InputMongodb(InputPlugin):
    
    def init_plugin(self, url: str, collection: str, conditions: dict):

        if url is None or type(url) != str:
            raise ValueError("url is required and must be string")

        if collection is None or type(collection) != str:
            raise ValueError("collection is required and must be string")

        self._client = pymongo.MongoClient(url)
        self._db = self._client.get_default_database()
        self._col = self._db.get_collection(collection)
        self._conditions = conditions or {}

    def load(self):
        return list(self._col.find(self._conditions))

