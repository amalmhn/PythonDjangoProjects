#KL08BS1375=> valid
#GJ08BN2210=>invalid

f=open('reg_numbers','r')
fout=open('validreg','w')
regnum=set()
for numbers in f:
    regnum.add(numbers.rstrip('\n'))
print(regnum)
from re import *

rule='KL\d{2}[A-Z]{1,2}\d{1,4}'

for vehiclenum in regnum:
    matcher=fullmatch(rule,vehiclenum)
    if matcher!=None:
        fout.write(vehiclenum+'\n')
    else:
        pass

#HW# create rule for validating email ids
# from file to file
#validate all phone numbers #

#package called beautifulsoap used for web scraping
#exceptionhandling
#mysql(create,insert,update,delete)
