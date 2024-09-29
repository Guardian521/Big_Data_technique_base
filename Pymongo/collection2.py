from sql_pymongo import db
col1 = db['gushuaitable2']
col1.insert_one({"name": "Ram", "age": "26", "city": "Hyderabad"})
col2 = db['coll']
col2.insert_one({"name": "Rahim", "age": "27", "city": "Bangalore"})
col3 = db['myColl']
col3.insert_one({"name": "Robert", "age": "28", "city": "Mumbai"})
col4 = db['data']
col4.insert_one({"name": "Romeo", "age": "25", "city": "Pune"})

#List of collections
print("删除集合前的所有集合")
collections = db.list_collection_names()
for coll in collections:
    print(coll)

col1.drop()
col4.drop()

print("删除两个集合前的所有集合")
#List of collections
collections = db.list_collection_names()
for coll in collections:
   print(coll)

