#class className
class Person:
    #attributes of person self.name,self.age,self.gender
    def set_person(self,name,age,gender): #initializing persons attributes
        self.name=name #person has name
        self.age=age
        self.gender=gender
    #methods

    def print_person(self):  #'self' keyword used to point the current object
        print('name',self.name)
        print('age', self.age)
        print('gender', self.gender)

#reference_name=Class()
#inside class it is method and outside it is function

obj=Person()
obj.set_person('ajay',25,'male')
obj.print_person()

obj1=Person()
obj1.set_person('vijay',26,'male')
obj1.print_person()

