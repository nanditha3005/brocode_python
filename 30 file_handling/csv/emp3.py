# collect data form user and write into file

import csv
fp=open("user.csv","w" ,newline="" )
csv_object=csv.writer(fp)
csv_object.writerow(["username" ,"email" ,"location"])
csv_object.writerow(["rahul","rahul@gmail.com","wayanad"])
csv_object.writerow(["sonia","sonia@gmail.com","kerala"])

csv_object.writerows([["priyanka","priyanka@gmail.com","bengaluru"],
["modi","modi@gmail.com","pune"]])

print("written succesfully!")





fp.close()