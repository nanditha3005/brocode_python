#default arguments= a default value for certain paramaeters 
#                   default is used when that argiment is ommited
#                   make your functions more flexible,reduces # of arguments
#                   1.Positional   2.DEFAULT  3.Keyword   4.Variable-length arguments
  

def net_price(list_price, discount, tax):
    return list_price *(1-discount) * (1+tax)

print(net_price(500,0, 0.05))             #525.0


#using default argument
def net_price(list_price, discount=0, tax=0.05):
    return list_price *(1-discount) * (1+tax)

print(net_price(500))                     #525.0
