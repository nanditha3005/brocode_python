import mysql.connector 

try:
    dbcon=mysql.connector.connect(host="localhost",user="root",password="root",database="dbone")
    mycursor=dbcon.cursor()
    sql_st='''
              insert into employee values (%s,%s,%s,%s) 
           '''
    data=[(102,'sonia',34000.45,'wayanad'),
          (103,'priyanka',47000.05,'Kerala'),
          (104,'modi',67000.43,'delhi'),
          (105,'amith',34000.45,'pune')]
    
    mycursor.executemany(sql_st,data)
    dbcon.commit()
    print("Data Inserted Succesfully")

except mysql.connector.DatabaseError as err:
    if err:
        print(err) 

finally:
    mycursor.close()
    dbcon.close()