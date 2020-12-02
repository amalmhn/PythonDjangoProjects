#values are stored in dictionary in form of key value pairs


students={'rol':100,'name':'ajay','course':'bca'}

#print student name
#to print this here, as this is a dictionary
#ajay is a fetch value, we have to use the corresponding key
print(students['name'])
#course
print(students['course'])

print('-------------------------------------------------------------------------')

for item in students:
    print(item,students[item]) #item is a variable
print('-------------------------------------------------------------------------')

for k,v in students.items(): #easiest method to get both key and values
    print(k,v)

print('-------------------------------------------------------------------------')

students['name']='AJAY'
print(students)

print('-------------------------------------------------------------------------')
#checking for a specific key
print('rol' in students)
print('total' in students)

print('-------------------------------------------------------------------------')
#adding a key and value to the dic
if ('total' not in students):
    students['total']=150
    print(students)

#adding another 50 to total
students['total']+=50
print(students)

print('-------------------------------------------------------------------------')

students1={100:{'rol':100,'name':'ajay','course':'bca'},101:{'rol':101,'name':'vijay','course':'bca'}}
print(students1)
#to print the particular values
print(students1[100]['name'])