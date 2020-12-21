lst=['java','python','c#','javascript']

print(lst)

print(lst[0])

print(lst[3])

print(lst[-1])

print(lst[0:3])

print('---------------------------------')
#list slicing (upper, lower, step)
print(lst[0:4:2])

#iteration
for item in lst:
    print(item)

#to add a new element to the list
lst.append("dart")

print(lst)

#UPDATE: to replace a value
lst[0]='Ruby'

print(lst)

#Can add duplicate values, for eg.
#lst=(python, python, python)


#inserting an object into a specific position
lst.insert(2, 'perl')
print(lst)


# ...HW...
# marks=list()
# insert some values
# perform slicing
# update a object

