from pymongo import MongoClient
from bson import json_util
import json

client = MongoClient("mongodb+srv://paulo:Paulao123@cluster0.nl7tfxi.mongodb.net/?retryWrites=true&w=majority")
db = client["free-games"]

def saveOne(collection_name, data):
    jsonData = json.loads(json_util.dumps(data))
    collection = db[collection_name]
    inserted = collection.insert_one(jsonData)
    return inserted.inserted_id