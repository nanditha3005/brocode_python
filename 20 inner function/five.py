#convert local as global variable
def funcone():
    global a
    a=100
    #print(a)

def functwo():
    print(a)

funcone()
functwo()             #100