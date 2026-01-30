from fastapi import APIRouter

router=APIRouter(prefix="/products")
from pydantic import BaseModel

class products(BaseModel):
    pid:int
    pname:str
    price:float
    qty:int
    info:str

'''
Create product
---------------
usage:create new product
API URL:"http://127.0.0.1:8000/product/create "
Method type:POST
Required filed:pid,pname,price,qty,info
Access type:public
'''
@router.post("/create")
def create_product():
    return {"msg":"New product created"}


'''
read product
---------------
usage:fetching all products
API URL:"http://127.0.0.1:8000/product/uid "
Method type:GET
Required filed:None
Access type:public
'''
@router.get("/{uid}")
def read_products(uid:int):
    return{"msg":"fetching all products","uid":uid}


'''
update product
---------------
usage:update product by id
API URL:"http://127.0.0.1:8000/product/update/uid "
Method type:PUT
Required filed:pid,pname,price,qty,info
Access type:public
'''
@router.put("/update/{uid}")
def update_product(uid:int):
    print(uid)
    return {"msg":"updated products succesfully","uid":uid}



'''
delete product
---------------
usage:delete product by id
API URL:"http://127.0.0.1:8000/product/delete/udi "
Method type:DELETE
Required filed:pid,pname,price,qty,info
Access type:public
'''
@router.delete("/delete/{uid}")
def delete_product(uid:int):
    return {"msg":"product deleted succesfuly","uid":uid}