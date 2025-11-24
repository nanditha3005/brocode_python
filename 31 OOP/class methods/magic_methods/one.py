# What Are Magic Methods ---  Magic methods (also called dunder methods – double underscore) are special methods in Python classes that have double underscores at the beginning and end of their names, like __init__, __str__, __add__, etc.
#                             They allow you to customize how your objects behave with Python’s built-in operations (like +, len(), print(), ==, etc.).
#                             You don’t call them directly — Python calls them automatically when you use certain syntax.


class Book:

    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


    def __lt__(self,other):
        return self.num_pages < other.num_pages

    def __gt__(self,other):
        return self.num_pages > other.num_pages

    def __add__(self,other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self,key):
        if key =="title":
            return self.title
        elif key =="author":
            return self.author
        elif key =="num_pages":
            return self.num_pages

        else:
            return f"key {key} was not found"





book1=Book("The Hobbit" ,"J.R.R. Tolien" ,310)
book2=Book("Harry Potter and the philoshoper" ,"J.K.Rowling", 223)
book3=Book("The Lion,the witch and the Wardrobe" ,"C.S.Lewis", 172)

print(book1)
print(book2)
print(book3)
print(book1 ==book2)                    #False
print(book2 < book3)                    #False #TypeError: '<' not supported between instances of 'Book' and 'Book' 
print(book1 > book2)                    #True

print(book1 + book2)                   #533
print("Lion" in book3)                #True
print("Lion" in book1)                #False
print("Rowling" in book2)             #True
print(book1['title'])                  #The Hobbit
print(book3['author'])                #C.S.Lewis
print(book2["num_pages"])             #223
print(book1["sound"])                 #key sound was not found