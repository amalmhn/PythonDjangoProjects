#i                       i
lst=[1,2,3,5,8,7,8,10,6,11]
#j                          j
#    0 1 2  3 4 5 6 7 8  9
for i in range(0,len(lst)):
    for j in range((i+1),len(lst)):
        if(lst[i]>lst[j]):#2>1
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)
#[1, 2, 3, 5, 6, 7, 8, 8, 10, 11]
# 0  1  2  3  4   5  6  7   8   9
# low      upp  mid              upp

low=0
upp=len(lst)-1


mid=(low+upp)//2
print(mid)#4
element=2
#10>lst[mid] 2>6
#case1 element>lst[mid]
    #low=mid+1
#case2:elemnt<lst[mid] 2<6
# upp=mid-1

#element=6
# element==lst[mid]
# print(element found)