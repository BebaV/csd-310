from pymongo.mongo_client import MongoClient

#connection to mongodb
url = "mongodb+srv://admin:admin@cluster0.69vpp.mongodb.net/pytech?retryWrites=true"
client = MongoClient(url)
db = client.pytech
students = db.students

#students.find()
#docs = db.students_name.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in students.find():
    print(doc)

students.find_one()
doc = students.find_one({"student_id": "1007"})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
print("Student ID:",doc["student_id"])
print("First Name:",doc["first_name"])
print("Last Name:",doc["last_name"])