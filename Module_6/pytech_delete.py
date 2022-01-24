
from pymongo.mongo_client import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vy4xh.mongodb.net/pytech?retryWrites=true&w=majority0"
client = MongoClient(url)
db = client.pytech

db.collection_name.find()

students.insert()
joan = {
    "student_id" : "1010",
    "first_name" : " joan ",
    "last_name" : "crawford"
}
db.students.find({"student_id" : "1010"})


db.collection_name.remove({"student_id" : "1010"})

db.collection_name.find()