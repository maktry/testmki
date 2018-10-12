from pymongo import MongoClient
import json

conn = MongoClient()
db = conn["tumblelog"]

# conn.list_database_names()
# for x in range(1,10):
#     print(str(db[x]))
# collection = db.myclassb
# //////////////// TO PRINT DB NAMES



xx =db.list_collections(include_system_collections=False)

for collect in xx:
    print (collect)
# /*/////////////////// TO PRINT COLLECTION - TABLES
#  WE HAVE HAVE TWO --USER AND --TYPE HERE.


collection =db.get_collection("post")

cursor= collection.find()
print(cursor.count())
print(type(cursor[1]))

for m in cursor[2]:
    print(m)
# #
for rec in cursor:
    print((rec["author"] ,"   :   ", rec["title"]))
# ////////////////// the above code to print somthing from the COLLECTION

collection.insert_one({"author":"aaaaaa", "title":"awesome"})

# ////////////////////// insert into mongodb


the_one = collection.find({"author":"aaaaaa"})
print("----------------------------- %s", type(the_one))
print(the_one[0])

# /////// find from mangodB
