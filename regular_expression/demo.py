first=[1,2,3,4,6,7,5]

data=[i+1 if i>5 else i-1 if i<5 else i for i in first]
print(data)