class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age

    def __str__(self):
        return self.name

p=Person(25,'Person1')

print(p)

#if we are printing an object __str__() method will execute

