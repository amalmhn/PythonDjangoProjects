f_in=open('email_id_verify','r')
f_out=open('verified_emails','w')
ver_emails=set()

from re import *

for emails in f_in:
    ver_emails.add(emails.rstrip('\n'))
print(ver_emails)



rule='[a-z0-9]*[._]*[a-z0-9]*@[a-z]*[.][a-z]*'
# rule='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
for verfied in ver_emails:
    matcher=fullmatch(rule,verfied)
    if matcher!=None:
        f_out.write(verfied+'\n')
    else:
        pass




