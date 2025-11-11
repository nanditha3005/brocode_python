def outer():

    def inner():
        print("Inner Function")

    #return 100,200
    
    #return "Hello Good Evening"
    return inner

inner_fun_ref=outer()
#print(result)             #(100, 200)                
inner_fun_ref()