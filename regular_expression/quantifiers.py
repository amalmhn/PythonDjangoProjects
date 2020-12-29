#quantifiers

from re import *

# pattern='a+' #check for a and more than one a
# pattern='a*' #a+ plus 0 occurance of a
# pattern='a?' #a plus zero number of a
# pattern='^a' #chk for starting with a
pattern='a$' #ending with a
# pattern='a{2,3}' #chck for min 2a and max 3a

# matcher=finditer(pattern,'aaaabaaaabaaaa')
# for match in matcher:
#     print(match.start())
#     print(match.group())

matcher=fullmatch(pattern,'aabaabaa')
if matcher!=None:
    print('given string is start with a')
else:
    print('sting is not starting with a')