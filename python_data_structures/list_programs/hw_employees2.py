employees=[[1001,'ajay','qa',1981,2003],
           [1002,'vijay','developer',1992,2008],
           [1003,'arun','qa',1989,2010],
           [1004,'amal','developer',2009,2014],
           [1004,'vimal','developer',1987,1989]]

#print all employees designation
for i in employees:
    print(i[1],",",i[2])

print('-------------------------------------------------------------------------------------')
#print all employees whose designation = developer
for i in employees:
    if i[2]=='developer':
        print(i[1])

print('-------------------------------------------------------------------------------------')
#print all employees those who are working in 1980s
for i in employees:
    if (i[3]>=1980):
        if i[4]<=1989:
            print(i[1])

print('-------------------------------------------------------------------------------------')
#print all employee details whose experience > 9 years

for i in employees:
    if i[4]-i[3]>=9:
        print(i[1])

