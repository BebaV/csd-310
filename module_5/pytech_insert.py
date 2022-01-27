from pymongo.mongo_client import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vy4xh.mongodb.net/pytech?retryWrites=true"
client = MongoClient(url)
db = client.pytech
students = db.students

frank = {"student_id" : "1007","first_name" : " frank ","last_name" : "sinatra"}
gene = {"student_id" : "1008","first_name" : "gene","last_name" : "kelly"}
judy = {"student_id" : "1009","first_name" : "judy","last_name" : "garland"}

frank_student_id = students.insert_one(frank).inserted_id
gene_student_id = students.insert_one(gene).inserted_id
judy_student_id = students.insert_one(judy).inserted_id

print("-- insert statements --")
print("inserted student record frank sinatra into the students collection with student id ", frank_student_id)
print("inserted student record gene kelly into the students collection with student id ", gene_student_id)
print("inserted student record judy garland into the students collection with student id ", judy_student_id)