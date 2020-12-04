pattern='ABABAC'

dict={}
for char in pattern:
    if char not in pattern:
        dict[char]=1
    else:
        print(char,'is the first recursive character')
        break

