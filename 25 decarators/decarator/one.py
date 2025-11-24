# decarator--- A function that extends the behaviour of another function without 
#              modifying the base function by
#              passing the base function as an argument to the decarator

def add_sprinkles(func):
    def wrapper(*args ,**kwargs):
        print("You add sprinkles ")
        func(*args ,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add funge")
        func(*args ,**kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_icecream(flavour):
    print(f"Here is your {flavour} Ice Cream!")

get_icecream("Vanilla")
get_icecream("Chocolate")
