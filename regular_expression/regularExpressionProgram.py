from re import *
###PREDIFEND CHARACTER SET##################
# pattern='[a-z]' #chk for lowercase a to z characters
pattern='[^0-9]' #"except" numbers
#pattern='[^a-z]' #"except" lowercase characters
# pattern='[a-zA-z]' #chk for both lowercase and uppercase
# pattern='[a-zA-z0-9]' #chk for lowercase, uppercase and digit
# pattern='[^a-zA-z0-9]' #chk for lowercase, uppercase and digit


###PREDIFEND CHARACTERS##################
# pattern='[\s]' #chk for spaces
# pattern='[\S]' #except spaces
# pattern='[\d]' #chk for digit
# pattern='[\D]' #except the digit
# pattern='[\w]' #[a-zA-z0-9]
# pattern='[\W]' #only special characters
matcher=finditer(pattern,'abc Z@7k')

for match in matcher:
    print(match.start()) #0 1 2
    print(match.group()) #a b c k


