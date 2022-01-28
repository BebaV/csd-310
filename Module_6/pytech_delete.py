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

joan = {"student_id" : "1010","first_name" : " joan","last_name" : "crawford"}
joan_student_id = students.insert_one(joan).inserted_id

print("-- Insert Statements --")
print("Inserted student record frank sinatra into the students collection with document_id ", joan_student_id,"\n")

db.students.find({"student_id" : "1010"})

students.find_one()
doc = students.find_one({"student_id": "1010"})

print("-- DISPLAYING STUDENT TEST DOC --")
print("Student ID:",doc["student_id"])
print("First Name:",doc["first_name"])
print("Last Name:",doc["last_name"],"\n")

students.delete_one({"student_id":"1010"})
#db.collection_name.remove({"student_id" : "1010"})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in students.find():
    print("Student ID:",doc["student_id"])
    print("First Name:",doc["first_name"])
    print("Last Name:",doc["last_name"],"\n")