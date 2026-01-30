#invoke rest api and insert all beauty products into mongodb database
#API url=https://dummyjson.com/products
#method type=GET

import requests
import pymongo
from pymongo import MongoClient

# extract
response=requests.get("https://dummyjson.com/products")
product_data=response.json()
products=product_data["products"]

# load
beauty_products=[]
# print(type(products))                     30
# print(len(products))                      <class:list>

for product in products:
    if product['category']=="beauty":
         beauty_products.append(product)

# print(len(beauty_products))                  5

# load
dbcon=pymongo.MongoClient('mongodb://localhost:27017/')
db=dbcon['dbone']

product_col=db["products"]
product_col.insert_many(beauty_products)
print("data inserted succesfully")
