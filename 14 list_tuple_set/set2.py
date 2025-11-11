ids={101,102,103,104}
ids.add(105)
print(ids)                #{101, 102, 103, 104, 105}--add item to set object

ids.update([10,20,30])
print(ids)                #{101, 102, 103, 104, 105, 10, 20, 30}--if u want to add multiple items/iterable object 

# enames={"rahul","sonia","priyanka","modi"}
# enames.update(10)          #TypeError: 'int' object is not iterable
# print(enames)


#-----------------------------------------
#delete  methods
ids={101,102,103,104}
ids.pop()                    #it removes random element from set
print(ids)                  #{101, 102, 103}

ids.remove(103)
print(ids)                   #{101,102,104}

# ids.remove(105)               #results in keyerror
# print(ids)

# ids.discard(105)              #results in any error
# print(ids)

ids.clear()
print(ids)



#-------------------------------------------
#set Operators

#union
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.union(s2))                  #{40, 10, 50, 20, 60, 30}
print(s1| s2)                        ##{40, 10, 50, 20, 60, 30}

#difference
s1={10,20,30,40}
s2={30,40,50,60}
print(s1 - s2)                         #{10, 20}
print(s1.difference(s2))               #{10, 20}


#intersection
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.intersection(s2))              #{40, 30}
print(s1 & s2)                          #{40, 30}


#symmetric difference
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.symmetric_difference(s2))           #{10, 50, 20, 60}
print(s1 ^ s2)                               #{10, 50, 20, 60}