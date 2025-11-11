#dict--group of key:value pairs
#      ordered and changable.no duplicates
capitals={"USA":"Washington dc",
          "India":"Delhi",
          "China":"Bejing",
          "Russia":"Moscow"}

#print(dir(capitals))
print(capitals.get("USA"))                    #Washingthon dc
print(capitals.get("japan"))                  #None

if capitals.get("japan"):
    print("That capital exist")
else:
    print("That capital doesnt exits")


capitals.update({"Grmany":"Berlin"})
print(capitals)                           #{'USA': 'Washington dc', 'India': 'Delhi', 'China': 'Bejing', 'Russia': 'Moscow', 'Grmany': 'Berlin'}

capitals.update({"USA":"Detroit"})
print(capitals)                           #{'USA': 'Detroit', 'India': 'Delhi', 'China': 'Bejing', 'Russia': 'Moscow', 'Grmany': 'Berlin'}

capitals.pop("China")
print(capitals)                           #{'USA': 'Detroit', 'India': 'Delhi', 'Russia': 'Moscow', 'Grmany': 'Berlin'}

capitals.popitem()
print(capitals)                            #{'USA': 'Detroit', 'India': 'Delhi', 'Russia': 'Moscow'}

capitals.clear() 
print(capitals)                            #{}


#-----------------------------
capitals1={"USA":"Washington dc",
          "India":"Delhi",
          "China":"Bejing",
          "Russia":"Moscow"}
key=capitals1.keys()
print(key)                                   #dict_keys(['USA', 'India', 'China', 'Russia'])

for key in capitals1.keys():
    print(key)                           #USA India China Russia

values=capitals1.values()
print(values)                                 #dict_values(['Washington dc', 'Delhi', 'Bejing', 'Moscow'])

for value in capitals1.values():
    print(value)                          #Washington dc Delhi Bejing Moscow


#------------------------------
items=capitals1.items()
print(items)                                #dict_items([('USA', 'Washington dc'), ('India', 'Delhi'), ('China', 'Bejing'), ('Russia', 'Moscow')])

for key,value in capitals1.items():
    print(f"{key}:{value}")                       #USA:Washington dc
                                                  #India:Delhi
                                                  #China:Bejing
                                                  #Russia:Moscow