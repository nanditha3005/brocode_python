try:
    number=int(input("Enter a number:"))
    print(1/number)

except ZeroDivisionError:
    print("You cant divide by zero!")

except ValueError:
    print("enter only numbers please")

finally:
    print("Do some clean up here!")