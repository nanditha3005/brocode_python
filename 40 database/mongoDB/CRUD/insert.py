import pymongo
from pymongo import MongoClient

dbcon=MongoClient('mongodb://localhost:27017')
db=dbcon['dbone']
user_col=db["users"]

user_col.insert_one({"uid":101,"uname":"rahul"})
print("data inserted suscesfully!")

user_col.insert_many({"uid":102,"uname":"sonia"},{"uid":103,"uname":"priyanka"},{"uid":104,"uname":"modi"})
print("second data inseted!")

dbcon.close()