employees=[[1001,'ajay','qa',15000],[1002,'vijay','developer',25000],[1003,'arun','ba',15000],
          [1004,'amal','developer',30000]]

#print employee id

for i in employees:
    print(i[0])

#find total of salary
salarySum=0
for i in employees:
    salarySum=salarySum+i[3]
print(salarySum)



#find how mant members working as developer
developer=0
for i in employees:
    if i[2]=='developer':
        developer+=1
print(developer)



#find total salary group by designation
qaSum=0
for i in employees:
    if (i[2]=='qa'):
        qaSum+=i[3]