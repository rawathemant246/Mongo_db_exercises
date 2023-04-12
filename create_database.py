import pymongo
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://localhost:27017')

def database():
    db =  client['wine_quality']
    collect = db['csv_file']