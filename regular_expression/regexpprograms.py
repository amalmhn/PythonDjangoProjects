#regular expression
#pattern matching
#step1
#package not built in builtins.py

import re
matcher=re.finditer('ab','ababababab')

# for match in matcher:
#     print(match.start())
#     print(match.group())

cnt=0
for match in matcher:
    print(match.start())
    print(match.group())
    cnt+=1
print('=============================')
print(cnt)