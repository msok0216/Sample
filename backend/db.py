from pymongo import MongoClient
from pprint import pprint
import os
import urllib
MONGO_URI = os.environ.get('MONGO_URI')
print(MONGO_URI)
client = MongoClient(MONGO_URI)




