#FILTER
#fetch only even numbers???
lst=[10,11,12,13,14,15]

even=list(filter(lambda no:no%2==0,lst))
print(even)

#???
names=['ajay','aji','binoy','abhi','anu']
na=list(map(lambda name:name.upper(),names))
print(na)

aname=list(filter(lambda name:name[0]=='a',names))
print(aname)