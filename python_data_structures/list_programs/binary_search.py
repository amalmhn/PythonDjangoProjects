lst=[2,1,5,8,7,6,8,10,3,11]

#step 1 we have to sort this array
#ascending order
for i in range(0,len(lst)):
    for j in range((i+1),len(lst)):
        if (lst[i]>lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp

print(lst)

low=0
upp=len(lst)-1

mid=(low+upp)//2 #// to remove the float value
print(mid)
element=10




