f_in=open('email_id_verify','r')
f_out=open('verified_emails','w')
ver_emails=set()

for emails in f_in:
    ver_emails.add(emails.rstrip('\n'))
print(ver_emails)

from re import *
print('Valid email Id')
rule='[a-z]{15}@[a-z].\w{1,3}]'

for emailid in ver_emails:
    matcher=fullmatch(rule,emailid)
    if matcher!=None:
        f_out.write(emailid+'\n')
    else:
        pass