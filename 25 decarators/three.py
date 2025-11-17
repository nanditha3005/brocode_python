def page_check(func):
    def inner(name,login):
        if login==False:
            print("Please try to login first")
        else:
            return func(name,login)
    return inner



def home_page(name,login):
    print("Home Page" ,name)

@page_check
def order_page(name,login):
    print("order Page" ,name)

@page_check
def payment_page(name,login):
    print("payment Page" ,name)


home_page("Rahul",True)
order_page("Sonia",True)
payment_page("Priyanka",False)
