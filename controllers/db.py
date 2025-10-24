import os
from pymongo import MongoClient

client = MongoClient(os.getenv('MONGO_API'))
db = client['Learning-Pymongo']

try:
    client.admin.command('ping')
    print(" --------------- MongoDB connection successful! --------------- ")
except Exception as e:
    print(f" --------------- MongoDB connection failed! - {e} --------------- ")

def get_db():
    collection = db['Users']
    try:
        yield collection
    finally:
        pass