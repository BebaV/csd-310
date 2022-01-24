from pymongo.mongo_client import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vy4xh.mongodb.net/pytech?retryWrites=true"
client = MongoClient(url)
db = client.pytech
mycol = db.students

students = [
    {"student_id" : "1007","first_name" : " frank ","last_name" : "sinatra"},
    {"student_id" : "1008","first_name" : "gene","last_name" : "kelly"},
    {"student_id" : "1009","first_name" : "judy","last_name" : "garland"}

]

mycol.insert_many(students).inserted_ids

#print(frank_student_id, gene_student_id, judy_student_id)


