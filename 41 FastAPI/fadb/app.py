from fastapi import FastAPI
from database import get_db_connection
from pydantic import BaseModel

app=FastAPI()

class Employee(BaseModel):
    eid:int
    ename:str
    esal:float


'''
Application Root
-----------------------
usage:appliaction root request
API URL:http://127.0.0.1:8000/
Method type:GET
Required fields:None
Access type:public
'''
@app.get("/")
def home_page():
    return{"msg":"Application root request"}


'''
Create
-----------------------
usage:create new employees
API URL:http://127.0.0.1:8000/emp/
Method type:POST
Required fields:eid,ename,esal
Access type:public
'''
@app.post("/emp")
async def create_emp(emp:Employee):
    dbcon=get_db_connection()
    cursor=dbcon.cursor()
    sql_st='insert into employees (eid,ename,esal) values(%s,%s,%s);'
    values=(emp.eid,emp.ename,emp.esal)
    cursor.execute(sql_st,values)
    dbcon.commit()
    dbcon.close()
    return{"msg":"New employee created"}



'''
read
----------------
Usage:fetch employees
REST API URL: 127.0.0.1:8000/emp/
Method Type:GET
Required Fields:None 
Access Type:Public 
'''
@app.get("/emp")
async def get_employees():
    dbcon=get_db_connection()
    cursor=dbcon.cursor()
    sql_st='Select * from employees;'
    cursor.execute(sql_st)
    employees=cursor.fetchall()
    dbcon.commit()
    return employees



'''
Update
----------
Usage: Update existing employee details
REST API URL: 127.0.0.1:8000/emp/{eid}
Method Type: PUT
Required Fields: eid,ename, esal
Access Type: Public
'''
@app.put("/emp/{eid}")
async def update_emp(eid:int,emp:Employee):
    dbcon=get_db_connection()
    cursor=dbcon.cursor()
    sql_st='update employees set ename =%s,esal=%s where eid=%s;'
    values=(emp.ename,emp.esal,eid)
    cursor.execute(sql_st,values)
    dbcon.commit()
    rows_affected =cursor.rowcount
    cursor.close()
    dbcon.close()

    if rows_affected == 0:
        return {"msg":f"No employee found with ID {eid}"}
    else:
        return {"msg":f"Employee with ID {eid} updated sucessfully"}
    


'''
Update
----------
Usage: Update existing employee details
REST API URL: 127.0.0.1:8000/emp/{eid}
Method Type: PUT
Required Fields: eid,ename, esal
Access Type: Public
'''
@app.delete("/emp/{eid}")
async def delete_emp(eid:int):
    dbcon=get_db_connection()
    cursor=dbcon.cursor()
    sql_st='delete from employees where eid=%s'
    cursor.execute(sql_st,(eid,))
    dbcon.commit()
    rows_affected=cursor.rowcount
    cursor.close()
    dbcon.close()

    if rows_affected == 0:
        return {"msg":f"No employee found with ID {eid}"}
    else:
        return{"msg":f"Employee with ID {eid} deleted succesfully"}