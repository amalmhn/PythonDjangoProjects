#find highest salary
from functools import *

class Employee:
    def __init__(self,eid,ename,desig,salary,exp):
        self.eid=eid
        self.ename = ename
        self.desig = desig
        self.salary = salary
        self.exp = exp

    def __str__(self):
        return self.ename

#reference file
f=open('employee','r')
employess=[]
for lines in f:
    #

    eid,ename,desig,salary,exp=lines.rstrip('\n').split(',')
    employess.append(Employee(eid,ename,desig,salary,exp))

print(employess)

highest=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
               list(map(lambda sala:sala.salary,employess)))
print(highest)
# for emp in employess:

#print highest salaried employee details

# employee=list(filter(lambda sala:sala.salary==highest,employess))
# for emp in employess:
#     print(emp.ename)

for emp in employess:
    if  emp.salary==highest:
        print(emp)

#find the highest salary of developer
developers=list(filter(lambda emp:emp.desig=='developer',employess))

devsalary=list(map(lambda emp:emp.salary,developers))

devhighest=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,devsalary)

print(devhighest)