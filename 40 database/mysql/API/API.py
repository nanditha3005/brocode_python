# invoke rest api ,amalyse data and insert into
# 1.csv file
# 2.json file
# 3.Mysql batabse
# 4.Mongodb database

# Rest api URL: https://jsonplaceholder.typicode.com/users
# Method type:
# acess type:
# required fields:

import requests
import pymongo
from pymongo import MongoClient

respone=requests.get("https://jsonplaceholder.typicode.com/users")
user_list=respone.json()
print(type(user_list))                       #<class 'list'>
print(user_list)

# print id,name,email
for user in user_list:
    # print(type(user))
    print(user["id"],user['name'],user['email'])