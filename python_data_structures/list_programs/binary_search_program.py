lst=[7,2,3,6,8,1,10]
#step1
lst.sort() #its a method inside the class named list
# lst=sorted(lst) #sorted is a function
element=int(input("Enter a number you want to search"))
print(lst)

low=0
upp=len(lst)-1
flg=0

while(low<=upp): #0<=6
    mid=(low+upp)//2 #3
    #case1
    if(element>lst[mid]): #10>6 10>7
        low=mid+1   #low=3+1=4  4+1=5
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flg=1
        break

if(flg>0):
    print("Found")
else:
    print("Not found")
