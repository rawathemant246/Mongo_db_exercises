import pymongo
from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017')

print(mongo_client.list_database_names())