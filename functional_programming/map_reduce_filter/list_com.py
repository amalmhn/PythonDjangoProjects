first=[1,2,3,4,6,7,5]
# second=[4,5,6]
#
# pairs=[(i,j)for i in first for j in second]
#
# print(pairs)


# square=[(i**2)for i in first]
# print(square)

# data=[i-1 if i<5 else i+1 for i in first]
# print(data)

data=[i+1 if i>5 else i-1 if i<5 else 0 if i==0 else i for i in first]
print(data)

#flatten operation
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flat=[j for i in matrix for j in i]
print(flat)