cars=[{"model":1,"brand":"Ludovika","price":800000,"color":"green"},
{"model":2,"brand":"Alidia","price":670000,"color":"green"},
{"model":3,"brand":"Garald","price":1000000,"color":"black"},
{"model":4,"brand":"Chloette","price":45000,"color":"green"},
{"model":5,"brand":"Bill","price":560000,"color":"purple"},
{"model":6,"brand":"Millard","price":450000,"color":"pink"},
{"model":7,"brand":"Dorolice","price":764300,"color":"black"},
{"model":8,"brand":"Joelynn","price":450000,"color":"blue"},
{"model":9,"brand":"Rhetta","price":1000000,"color":"green"},
{"model":10,"brand":"Fleming","price":340000,"color":"yellow"}]

def filter_cars(car):
    if car['price']<100000:
        return True
    else:
        return False
below_10_lacs=list(filter(filter_cars,cars))
print(below_10_lacs)


print(list(filter(lambda car:cars.color=="green",cars)))
