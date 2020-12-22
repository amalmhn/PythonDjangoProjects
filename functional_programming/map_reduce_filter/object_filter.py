class Employee:
    def __init__(self,id,name,salary,desig):
        self.id=id
        self.name = name
        self.salary = salary
        self.desig = desig

    def __str__(self):
        return self.name


obj1=Employee(100,'ajay',25000,'developer')
obj2=Employee(101,'vijay',20000,'developer')
obj3=Employee(102,'binoy',22000,'qa')

#convert empolyee name upper case

lst=[]
lst.append(obj1)
lst.append(obj2)
lst.append(obj3)
# for emp in lst:
#     print(emp)
print(lst)
upnames=list(map(lambda emp:emp.name.upper(),lst))
print(upnames)