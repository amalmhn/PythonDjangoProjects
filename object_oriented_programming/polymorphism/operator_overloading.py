class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):#to add two classes
        return Book(self.pages+other.pages)

    def __str__(self): #in __init__ you need to give this __str__ otherwise wont work
        return str(self.pages)

b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(400)
print(b1+b2+b3+b4)

print(type(b1))
