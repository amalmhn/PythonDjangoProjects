class Parent:
    def phone(self):
        print('have nokia 5310')

class Child(Parent):
    def phone(self):
        print('have nokia iphone 12')
    pass

c=Child()
c.phone()

#This is method overriding
#A Parent and child class relationship should be there for overriding
#