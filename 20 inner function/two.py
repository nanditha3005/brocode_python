def mall():
    pass

    def store1():
        pass
    def store2():
        pass
 
    print(id(store1))             #2043753921936
    print(id(store2))             #2043753922368
 
mall()                            #2158261501328
print(id(mall()))                 #140705504147448