#variable name NEW rule
#starting with alphabet a-k
#second char should be a digit and it must be divisible by 3
#followed by any number of characters
# z2rggg=>invalid
#B7vggg=>invalid
#a3rggg=>valid

from re import *
rule='[a-kA-K][369][a-zA-Z0-9]*' #or you can use \w. * is for unlimited char

variable_name=input('enter variable name')

matcher=fullmatch(rule,variable_name) #if there is no full match then it is none
                                        # You can use the match instead of
#                                       fullmatch to avoid the * in rule
if matcher!=None:
    print('valid variable name')
else:
    print('invalid')