import json
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:47230/AAC' % (username, password))
        self.database = self.client['AAC']

    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # Inserting data into animals collection
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data) # Reading data from animals collection
        else:
            raise Exception('Nothing to read, because data parameter is empty')
            return False
    
    def readAll(self, data):
        if data is not None:
            result = list(self.database.animals.find(data, {"_id": False}))
            return result# Reading data from animals collection
        else:
            raise Exception('Nothing to read, because data parameter is empty')
            return False

    def update(self, data, newData):
        if data is not None:
            print("Update successful")
            return self.database.animals.update_many(data, {'$set':newData}) # Updating data from animals collection
        else:
            raise Exception("Nothing to update, because parameter is empty")

    def delete(self, data):
        if data is not None:
            print("Delete successful")
            self.database.animals.delete_one(data) # Deleting data from animals collection
        else:
            raise Exception("Nothing to delete, because parameter is empty")