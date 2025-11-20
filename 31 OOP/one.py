from car import Car

car1=Car("Mustang",2024,"Blue",False)
car2=Car("Inova",2023,"red",True)

print(car1)                               #<__main__.car object at 0x00000224BACDBF40>
print(car1.model)                         #Mustang
print(car1.year)                          #2024
print(car1.color)                         #Blue
print(car1.for_sale)                      #False

# car1.drive()
# car2.drive()
# car1.stop()
# car2.stop()

# car1.drive()                         #You drive the Mustang
# car1.stop()                          #You stop the Mustang!
# car2.drive()                         #You drive the Inova
# car2.stop()                          #You stop the Inova!

car1.drive()                           #You drive the Blue Mustang
car2.stop()                            #You stop the  red Inova!


car1.describe()                        #2024 Blue Mustang
car2.describe()                        #2023 red Inova