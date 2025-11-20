class Account:
    min_bal=500                               #class varaible

    def __init__(self,id):
        self.acc_id=id                        #instance variable
        Account.branch_name="Marathalli"      #class/static variable      inside a construtor--using classname
    
    def set_branchID(self):
        Account.branchID=6777                # inside a instance method--using classname

    @classmethod
    def update_parentbranch(cls):
        cls.parentbranch="Bengaluru"         # inside classmethod--using cls and classname

    @staticmethod
    def tax_cal():
        Account.tax=10                       # inside a static method--using classname

    #where to define a class- inside a class outside any method

a1=Account(101)
a2=Account(102)
# print(a1.__dict__)                  #{'acc_id': 101}
print(Account.__dict__)              #{'__module__': '__main__', 'min_bal': 500, '__init__': <function Account.__init__ at 0x000002321FC7FF40>, 'set_bal': <function Account.set_bal at 0x000002321FC7FEB0>, 'update_minbal': <classmethod(<function Account.update_minbal at 0x000002321FC90160>)>, '__dict__': <attribute '__dict__' of 'Account' objects>, '__weakref__': <attribute '__weakref__' of 'Account' objects>, '__doc__': None, 'branch_name': 'Marathalli'}


a1.set_branchID()
a1.update_parentbranch()
a1.tax_cal()
print(Account.__dict__)              #{'__module__': '__main__', 'min_bal': 500, '__init__': <function Account.__init__ at 0x0000014CC337FF40>, 'set_branchID': <function Account.set_branchID at 0x0000014CC337FEB0>, 'update_parentbranch': <classmethod(<function Account.update_parentbranch at 0x0000014CC3390160>)>, 'tax_cal': <staticmethod(<function Account.tax_cal at 0x0000014CC33900D0>)>, '__dict__': <attribute '__dict__' of 'Account' objects>, '__weakref__': <attribute '__weakref__' of 'Account' objects>, '__doc__': None, 'branch_name': 'Marathalli', 'branchID': 6777, 'parentbranch': 'Bengaluru', 'tax': 10}





#how to create class variable:

# inside a construtor      --using classname
# inside a instance method--using classname
# inside classmethod      --using cls and classname
# inside a static method  --using classname