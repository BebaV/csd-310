from pymongo.mongo_client import MongoClient

#connection to mongodb
url = "mongodb+srv://admin:admin@cluster0.vy4xh.mongodb.net/pytech?retryWrites=true&w=majority0"
client = MongoClient(url)
db = client.pytech
students = db.students

students.find()
docs = db.students_name.find({})

for doc in docs:
    print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
    print(docs)

students.find_one()
doc = students.find_one({"student_id": "1007"})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
print("Student ID:",doc["student_id"])
print("First Name:",doc["first_name"])
print("Last Name:",doc["last_name"])