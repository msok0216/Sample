from pymongo import MongoClient
from pprint import pprint

client = MongoClient("URL")

def get_db():
    client = MongoClient("MongoDB URL")
    return client



