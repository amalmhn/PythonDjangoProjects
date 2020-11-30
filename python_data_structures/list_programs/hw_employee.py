employees=[[1001,'ajay','qa',15000],[1002,'vijay','developer',25000],[1003,'arun','qa',15000],
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
cnt=0
for i in employees:
    if i[2]=='developer':
        cnt+=1
print(cnt)



#find total salary group by designation
qaSum=0
deSum=0
for i in employees:
    if (i[2]=='qa'):
        qaSum+=i[3]
    if (i[2]=='developer'):
        deSum+=i[3]
print(qaSum)
print(deSum)
