import pymongo
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('mongodb://localhost:27017')

def database(db, collect):
    db =  client['wine_quality']
    collect = db['csv_file']
    return collect

a =12
b =13

