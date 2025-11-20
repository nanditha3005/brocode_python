class Test:
    a=100                    #class
    def m1(self):
        self.b=200           #instance
        c=300                #local
        print(c)

    def m2(self):
        pass
        # print(c)           NameError

t1=Test()
t1.m1()
