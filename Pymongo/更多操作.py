from sql_pymongo import db
import pymongo
#查询

col1 = db.Homework4_2216113486_谷帅_名人名言
print("Collection ({}) created........".format(col1))
re=col1.find({})
for i in re:
    print(i)
'''
doc1 = {"name": "Ram",
        "age": "26",
        "city": "Hyderabad"}

col1.insert_one(doc1)
print(col1.find_one())
data = [
   {
      "_id": "1000011",
      "name": "Ram",
      "age": "26",
      "city": "Hyderabad"
   },
   {
      "_id": "10000012",
      "name": "Rahim",
      "age": "27",
      "city": "Bangalore"
   },
   {
      "_id": "10000013",
      "name": "Robert",
      "age": "28",
      "city": "Mumbai"
   }
]
result = col1.insert_many(data,ordered=False)
'''

'''
result1 = col1.find_one({'name': 'Rahim'})
print(type(result1))
print(result1)

results = col1.find({'age':"26"})
print(type(results))
print(results)
for result in results:
   print(result)


results = col1.find({'age':{'$gt':"20"}})
# print(type(results))
print(results)
for result in results:
   print(result)

results = col1.find({'name': {'$regex': '^R.*'}})
# print(type(results))
print(results)
for result in results:
   print(result)

'''
'''
#排序
col1.find().sort("key1")

col1.find().sort("key1",pymongo.ASCENDING)
re=col1.find().sort("key1",pymongo.DESCENDING)

for i in re:
    print(i)
print("sort by age")
for doc1 in col1.find().sort("age"):
   print(doc1)

#找到后按年龄排序
print("sort by id")
for doc1 in col1.find().sort("_id"):
   print(doc1)

col1.find().sort([("key1", pymongo.ASCENDING), ("key2", pymongo.DESCENDING)])
print("sort by id and age")
for doc1 in col1.find().sort([("_id", pymongo.ASCENDING), ("age", pymongo.DESCENDING)]):
   print(doc1)
'''


'''
#删除
#Retrieving all the records using the find() method
print("删除前数据: ")
for doc2 in col1.find():
   print(doc2)


#删除一个记录，Deleting one document
col1.delete_one({"_id" : "1000011"})

print("删除后数据: ")
for doc2 in col1.find():
   print(doc2)

#Retrieving all the records using the find() method
print("删除前数据:  ")
for doc2 in col1.find():
   print(doc2) 

#删除多个记录，年龄大于26的 Deleting multiple documents
col1.delete_many({"age":{"$gt":"0"}})

#Retrieving all the records using the find() method
print("删除后数据:  ")
for doc2 in col1.find():
   print(doc2) 



#更新
#更改10000012城市， 注意在更新前需要重新插入数据
print("Documents in the collection: ")
print(list(col1.find({"_id":"1004"})))
col1.update_one({"_id":"10000012"},{"$set":{"city":"Visakhapatnam"}})
print(list(col1.find({"_id":"10000012"})))
col1.update_one({"_id":"10000012"},{"$set":{"city":"Madakasika"}})
print(list(col1.find({"_id":"10000012"})))

#更改所有100*id的城市Retrieving all the records using the find() method
print("更新前数据 ")
for doc1 in col1.find():
    print(doc1)

    #col1.update_many({"_id",{"$age":"26"}},{"$set":{"city":"Visakhapatnam"}})
col1.update_many({},{"$set":{"city":"Visakhapatnam"}})


print("更新后数据 ")
for doc2 in col1.find():
   print(doc2)


#计数
count = col1.count_documents({'age': "26"})
print(count)
'''