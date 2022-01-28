from pymongo.mongo_client import MongoClient

#connection to mongodb
url = "mongodb+srv://admin:admin@cluster0.69vpp.mongodb.net/pytech?retryWrites=true"
client = MongoClient(url)
db = client.pytech
students = db.students

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in students.find():
    print("Student ID:",doc["student_id"])
    print("First Name:",doc["first_name"])
    print("Last Name:",doc["last_name"],"\n")

#students.update_one()
result = db.students.update_one({"student_id": "1007"}, {"$set":{"last_name":"Hotsauce"}})

students.find_one()
doc = students.find_one({"student_id": "1007"})

print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
print("Student ID:",doc["student_id"])
print("First Name:",doc["first_name"])
print("Last Name:",doc["last_name"],"\n")