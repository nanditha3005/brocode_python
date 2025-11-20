import json

fp1=open("emp.json","r")
fp2=open("users.json","w")
users=json.load(fp1)

female_users=[]
for user in users:
    if user['gender']=="Female":
        female_users.append(user)

print(len(female_users))
print(female_users)
json.dump(female_users,fp2)
print("New JSON data created")

fp1.close()
fp2.close()


# 21
# [{'eid': 4, 'ename': 'Hildegaard', 'email': 'hrottgers3@seattletimes.com', 'gender': 'Female'}, {'eid': 5, 'ename': 'Rorie', 'email': 'rjanousek4@ca.gov', 'gender': 'Female'}, {'eid': 6, 'ename': 'Clementine', 'email': 'cbagwell5@google.com.au', 'gender': 'Female'}, {'eid': 7, 'ename': 'Heidi', 'email': 'hpantry6@meetup.com', 'gender': 'Female'}, {'eid': 10, 'ename': 'Wilhelmina', 'email': 'wlewin9@domainmarket.com', 'gender': 'Female'}, {'eid': 15, 'ename': 'Kari', 'email': 'kdelaguae@ow.ly', 'gender': 'Female'}, {'eid': 19, 'ename': 'Audre', 'email': 'aharrowi@apache.org', 'gender': 'Female'}, {'eid': 20, 'ename': 'Chickie', 'email': 'crackamj@google.com.hk', 'gender': 'Female'}, {'eid': 22, 'ename': 'Casi', 'email': 'cscreasl@github.io', 'gender': 'Female'}, {'eid': 23, 'ename': 'Aurel', 'email': 'arosenhausm@jalbum.net', 'gender': 'Female'}, {'eid': 26, 'ename': 'Rubetta', 'email': 'rinnisp@plala.or.jp', 'gender': 'Female'}, {'eid': 29, 'ename': 'Joyce', 'email': 'jbreznovics@instagram.com', 'gender': 'Female'}, {'eid': 35, 'ename': 'Clara', 'email': 'cmullordy@fc2.com', 'gender': 'Female'}, {'eid': 36, 'ename': 'Maureen', 'email': 'mmalonez@studiopress.com', 'gender': 'Female'}, {'eid': 37, 'ename': 'Kipp', 'email': 'kterzo10@theatlantic.com', 'gender': 'Female'}, {'eid': 38, 'ename': 'Clo', 'email': 'coshea11@who.int', 'gender': 'Female'}, {'eid': 39, 'ename': 'Milena', 'email': 'mmoon12@lycos.com', 'gender': 'Female'}, {'eid': 40, 'ename': 'Renae', 'email': 'rgeach13@prlog.org', 'gender': 'Female'}, {'eid': 43, 'ename': 'Joellyn', 'email': 'jmayoral16@tiny.cc', 'gender': 'Female'}, {'eid': 48, 'ename': 'Candide', 'email': 'cmacarthur1b@discuz.net', 'gender': 'Female'}, {'eid': 50, 'ename': 'Jerrylee', 'email': 'jocahill1d@engadget.com', 'gender': 'Female'}]
# New JSON data created