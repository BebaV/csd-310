from pymongo.mongo_client import MongoClient

#connection to mongodb
url = "mongodb+srv://admin:admin@cluster0.69vpp.mongodb.net/pytech?retryWrites=true"
client = MongoClient(url)
db = client.pytech
students = db.students

db.students_name.find()

db.students_name.update({“student_id”: 1007}, {“$set”: {“last_name”: ““Gorshin”}})

result = db.collection.find({Module_6/pytech_update.py})
print(result)