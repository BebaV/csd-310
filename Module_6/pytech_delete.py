from pymongo.mongo_client import MongoClient

#connection to mongodb
url = "mongodb+srv://admin:admin@cluster0.69vpp.mongodb.net/pytech?retryWrites=true"
client = MongoClient(url)
db = client.pytech
students = db.students

db.collection_name.find()

students.insert()
joan = {
    "student_id" : "1010",
    "first_name" : " joan",
    "last_name" : "crawford"
}
db.students.find({"student_id" : "1010"})


db.collection_name.remove({"student_id" : "1010"})

db.collection_name.find()