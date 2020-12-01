#       hw
names=['a','b','c','d','e','f']
passed=['a','b','c']

names=set()
passed=set()

names={'a','b','c','d','e','f'}
passed={'a','b','c'}

failed=names.difference(passed)

print(failed)