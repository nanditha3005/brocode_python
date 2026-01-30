import mysql.connector

try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",database="dbone")
    mycursor=dbcon.cursor()
    mycursor.execute('select * from employee')
    empdata=mycursor.fetchall()
    for emp in empdata:
        # print(emp)
        print("Employee id:",emp[0],
              "Employee name:",emp[1] ,
              "Employee salary:",emp[2] ,
              "Employee location:",emp[3])

    

except mysql.connector.DatabaseError as err:
    if err: 
        print(err)

finally:
    pass