#keyword arguments= an argument precedded by an identifier
#                   help with readability
#                   order of arguments doesnt matter

def hello(greeting,title,first_name,last_name):
    print(f"{greeting} {title}{first_name} {last_name}")

hello( "Hello", title="Mr.", first_name="Spongebob" ,last_name="Squarepants" )


for x in range(1,11):
    print(x,end=" ")

print()
print("1","2","3","4","5",sep="-")