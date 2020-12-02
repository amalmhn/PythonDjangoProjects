employee={'emp_id':1001,'emp_name':'Amal','desig':'developer','salary':25000}

#print employee name
print(employee['emp_name'])

#check exp key is there
print('exp' in employee)

#Add exp key to the dict
if ('exp' not in employee):
    employee['exp']=5
    print(employee)

#Add 5000 to salary
employee['salary']+=5000
print(employee['salary'])

#print key and values
for k,v in employee.items():
    print(k,',',v)