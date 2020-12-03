text='hello hai hai hello hai'
#o/phello:2 hai:3

words=text.split(' ')

print(words)

# cnt=0
# cnt_hai=0
# for i in words:
#     if i=='hello':
#         cnt+=1
# print(cnt)
#
# for i in words:
#     if i=='hai':
#         cnt_hai+=1
# print(cnt_hai)

dict={}

for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1

print(dict)


