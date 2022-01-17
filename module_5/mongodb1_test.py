import pymongo

url="mongodb+srv://admin:admin@cluster0.69vpp.mongodb.net/pytech?retryWrites=true&w=majority"
client=pymongo.MongoClient(url)
db=client.pytech
print(db.list_collection_names)
