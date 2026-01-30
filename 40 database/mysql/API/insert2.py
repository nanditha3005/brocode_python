import requests 
import mysql.connector

mycursor=None
dbcon=None

try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",database="dbone")
    mycursor=dbcon.cursor()
    sql_st='''
            insert into products (pid,pname,price,brand) values(%s,%s,%s,%s)
           '''
    data=[]
    response=requests.get("https://dummyjson.com/products")
    product_dict=response.json()
    # print(type(product_dict))    <class :dict>

    for product in product_dict['products']:
        data.append((product['id'],product['rating'],product['price'],product['category']))

    mycursor.executemany(sql_st,data)
    dbcon.commit()
    print("Data inserted succesfully!")
    

except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    if mycursor:
        mycursor.close()

    if dbcon:
        dbcon.close()



# create table products(
#     -> pid int,
#     -> rating float,
#     -> price int,
#     -> category varchar(32)
#     -> )
#     -> ;