import mysql.connector

# print(help('modules'))      to check whether a module is installed or not

try:
    dbcon=mysql.connector.connect(host="localhost",
                        user="root",
                        password="root",
                        database="dbone")
    
    mycursor=dbcon.cursor()
    sql_st='''
            create table employee(
            eid int,
            ename varchar(32),
            esal float,
            eloc varchar(32)
            );
           '''
    mycursor.execute(sql_st)
    dbcon.commit()
    print("Table created succesfully")



except mysql.connector.DatabaseError as err:
    if err:
        print(err)
    

finally:
    mycursor.close()
    dbcon.close()
