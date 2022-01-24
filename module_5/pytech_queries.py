
from pymongo.mongo_client import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vy4xh.mongodb.net/pytech?retryWrites=true&w=majority0"
client = MongoClient(url)
db = client.pytech

docs = db.find({})
print(docs)

find_one()
students.find_one({“student_id”: “1007”})
