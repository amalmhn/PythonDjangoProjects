lst=[7,2,3,6,8,1,10]
#step1
lst.sort() #its a method inside the class named list
# lst=sorted(lst) #sorted is a function
element=int(input("Enter a number you want to search"))
print(lst)

low=0
upp=len(lst)-1
flg=0

while(low<=upp): #0<=6  4<=6    4<=4
    mid=(low+upp)//2    #3  5   4
    #case1
    if(element>lst[mid]):   #7>6    7>8...
        low=mid+1   #4
    elif(element<lst[mid]): #7<8
        upp=mid-1   #4
    elif(element==lst[mid]):
        flg=1
        break

if(flg==1):
    print("Found")
else:
    print("Not found")

