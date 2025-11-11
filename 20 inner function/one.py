def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()     
    inner()


outer()
#Outer function
#Inner function
#Inner function