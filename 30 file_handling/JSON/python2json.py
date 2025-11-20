import json

emp_dict={
    'eid':101,
    'ename':"Sonia",
    'esal':45000,
    'avail':True
}
emp_json=json.dumps(emp_dict)
print(type(emp_dict))                       #<class 'dict'>
print(emp_dict)                             #{'eid': 101, 'ename': 'Sonia', 'esal': 45000, 'avail': True}
print(emp_json)                             #{"eid": 101, "ename": "Sonia", "esal": 45000, "avail": true}
