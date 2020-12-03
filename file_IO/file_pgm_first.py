#file operations are Read r, Write w and Append a (MAIN OPRTNS)

#step1 create reference
#reference_name=open(filepath,mode_of_operation)
f=open('names','r')

# for lines in f:
#     print(lines)
lst=[]
for lines in f:
    lst.append(lines.rstrip('\n'))
print(lst)

#rstrip and lstrip function
# data='hello\n'
# data=data.rstrip('\n')
# print(data)
