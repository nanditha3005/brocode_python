class employee:
    def __init__(self,id,name):
        self.eid=id
        self.ename=name         #creating inside a contructor-using self   

    def set_salary(self,sal):
        self.esal=sal           #creating inside a instance variable-using self   


a1=employee(101,"rahul")
a2=employee(102,"sonia")    

print(a1.__dict__)                   #{'eid': 101, 'ename': 'rahul'}
print(a2.__dict__)                   #{'eid': 102, 'ename': 'sonia'}

a1.set_salary(45000)
a2.set_salary(34000)
print(a1.__dict__)                   #{'eid': 101, 'ename': 'rahul', 'esal': 45000}
print(a2.__dict__)                   #{'eid': 102, 'ename': 'sonia', 'esal': 34000}

a1.eloc="Wayanad"  #creating outside a class--using object reference   
print(a1.__dict__)                   #{'eid': 101, 'ename': 'rahul', 'esal': 45000, 'eloc': 'Wayanad'}
print(a2.__dict__)                   #{'eid': 102, 'ename': 'sonia', 'esal': 34000}