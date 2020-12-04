f=open('word_data','r')

dict={}
for lines in f:
    print(lines)
    words=lines.rstrip('.\n').split(' ')
    print(words)
    break

for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1

for k,v in dict.items():
    print(k,v)

#to get the highest repeated word
highest=max(dict,key=dict.get) #'get' to fetch the value #dict.get hepls to fetch all the key values of a dict
print(dict[highest],highest)