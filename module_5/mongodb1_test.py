from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vy4xh.mongodb.net/pytech?retryWrites=true&w=majority0"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names())
