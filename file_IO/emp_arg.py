f=open('employee','r')
emp_dict={}

for lines in f:
    print(lines)

    id,name,desig,exp,salary=lines.rstrip('\n').split(',')
    # print(data)
    if id not in emp_dict:
        emp_dict[id]={'id':id,'name':name,'desig':desig,'exp':exp,'salary':salary}

print(emp_dict)
