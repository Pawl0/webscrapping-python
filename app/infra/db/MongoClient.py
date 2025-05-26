from pymongo import MongoClient
from bson import json_util
import json
import os

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")

print(os.environ)
print(db_user)
print(db_password)

client = MongoClient(f"mongodb+srv://{db_user}:{db_password}@cluster0.nl7tfxi.mongodb.net/?retryWrites=true&w=majority")
db = client["free-games"]

def saveOne(collection_name, data):
    jsonData = json.loads(json_util.dumps(data))
    collection = db[collection_name]
    inserted = collection.insert_one(jsonData)
    return inserted.inserted_id

def getLast(collection_name):
    data = db[collection_name].find().sort('_id', -1)[0]
    jsonDump = json_util.dumps(data)
    jsonLoaded = json.loads(jsonDump)
    print(jsonLoaded)
    return jsonLoaded