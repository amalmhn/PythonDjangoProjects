f=open('hw_phn_numbers','r')
f_out=open('verified_numbers','w')
ver_numbers=set()

from re import *

for numbers in f:
    ver_numbers.add(numbers.rstrip('\n'))
print(ver_numbers)

rule='\d{10}'

for num_ver in ver_numbers:
    matcher=fullmatch(rule,num_ver)
    if matcher!=None:
        f_out.write(num_ver+'\n')
    else:
        pass
