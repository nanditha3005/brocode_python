import mysql.connector

try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",database="dbone")
    mycursor=dbcon.cursor()
    sql_st='''
            delete from employee where eid=103;
           '''
    mycursor.execute(sql_st)
    dbcon.commit()
    print("Data deleted succesfully")

except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    mycursor.close()
    dbcon.commit()

