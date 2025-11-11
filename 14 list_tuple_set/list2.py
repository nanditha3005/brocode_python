# difference between append(),insert(),extend()

enames=["rahul","sonia","modi","priyanka"]
# enames.append('amith')
# print(enames)              ['rahul', 'sonia', 'modi', 'priyanka', 'amith']


# enames.insert(1, "satish")    
# print(enames)          #['rahul', 'satish', 'sonia', 'modi', 'priyanka']


new_names=["madu","girish","hishol","nagraj"]
enames.extend(new_names)

print(enames)           #['rahul', 'sonia', 'modi', 'priyanka', 'madu', 'girish', 'hishol', 'nagraj']