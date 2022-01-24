from pymongo.mongo_client import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vy4xh.mongodb.net/pytech?retryWrites=true"
client = MongoClient(url)
db = client.pytech
mycol = db.students

students = [
    {"student_id" : "1007","first_name" : " frank ","last_name" : "sinatra"},
    {"student_id" : "1008","first_name" : "gene","last_name" : "kelly"},
    {"student_id" : "1009","first_name" : "judy","last_name" : "garland"}
#frank = {"student_id" : "1007","first_name" : " frank ","last_name" : "sinatra"}
#gene = {"student_id" : "1008","first_name" : "gene","last_name" : "kelly"},
#judy = {"student_id" : "1009","first_name" : "judy","last_name" : "garland"}
]


#frank_student_id = mycol.insert_many(students).inserted_id
mycol.insert_many(students).inserted_ids
#gene_student_id = mycol.insert_one(gene).inserted_id
#judy_student_id = mycol.insert_one(judy).inserted_id

#print(frank_student_id, gene_student_id, judy_student_id)


