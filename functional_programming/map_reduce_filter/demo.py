class Employee:
    def __init__(self,id,name,desig,salary):
        self.name=name
        self.id = id
        self.desig = desig
        self.salary = salary

    def __str__(self):
        return self.name

obj1=Employee(100,'ajay',25000,'developer')
obj2=Employee(101,'vijay',20000,'developer')
obj3=Employee(102,'binoy',22000,'qa')

lst=[]

lst.append(obj1)
lst.append(obj2)
lst.append(obj3)

print(lst)

upname=list(map(lambda emp:emp.name.upper(),lst))
print(upname)
