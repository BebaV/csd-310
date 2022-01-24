from pymongo.mongo_client import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vy4xh.mongodb.net/pytech?retryWrites=true&w=majority0"
client = MongoClient(url)
db = client.pytech

students.insert()
frank = {
    "student_id" : "1007",
    "first_name" : " frank ",
    "last_name" : "sinatra"
}, ;
gene = {
    "student_id" : "1008",
    "first_name" : "gene",
    "last_name" : "kelly"
}, ;
judy = {
    "student_id" : "1009",
    "first_name" : "judy"
    "last_name" : "garland"
},
)
frank_student_id = students.insert_one(frank).inserted_id
gene_student_id = students.insert_one(gene).inserted_id
judy_student_id = students.insert_one(judy).inserted_id
