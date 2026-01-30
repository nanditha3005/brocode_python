import mysql.connector

try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",database="dbone")
    mycursor=dbcon.cursor()
    sql_st='''
            insert into employee values (101,'rahul',45000.00,'Bengaluru')
           '''
    mycursor.execute(sql_st)
    dbcon.commit()
    print("Data inserted succesfully")


except mysql.connector.DatabaseError as err:
    if err:
        print(err)
    
finally:
    mycursor.close()
    dbcon.close()
