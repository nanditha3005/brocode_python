from script1 import *

def favorite_Drink(drink):
    print(f"Your favorite drink is {drink}")


def main():
    print("This is Script2")
    favorite_food("Sushi")
    favorite_Drink("Coffee")
    print("Goodbye!")

if __name__  == '__main__':
    main()