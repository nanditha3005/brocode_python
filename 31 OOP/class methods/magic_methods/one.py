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

book1=Book("The Hobbit" ,"J.R.R. Tolien" ,310)
book2=Book("Harry Potter and the philoshoper" ,"J.K.Rowling", 223)
book3=Book("The Lion,the witch and the Wardrobe" ,"C.S.Lewis", 172)

print(book1)
print(book2)
print(book3)
print(book1 ==book2)