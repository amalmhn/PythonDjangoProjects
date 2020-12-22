lst=[10,11,12,13,14,15]

#if you want to do some function in all elements in the list

#squares
#map(function,iterable)

def squ(no):
    return no**2
#
# squares=list(map(lambda no:no**2,lst))
# print(squares)
#
squares=list(map(squ,lst))
print(squares)

#lambda helps to reduce the unwanted functions

cubes=list(map(lambda no:no**3,lst))
print(cubes)

print('------------------------------')

#FILTER
#fetch only even numbers???

even=list(filter(lambda no:no%2==0,lst))
print(even)

#???
names=['ajay','aji','binoy','abhi','anu']
na=list(map(lambda name:name.upper(),names))
print(na)

aname=list(filter(lambda name:name[0]=='a',names))
print(aname)
