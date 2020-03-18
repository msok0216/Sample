from pymongo import MongoClient
from pprint import pprint
import os
MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)




