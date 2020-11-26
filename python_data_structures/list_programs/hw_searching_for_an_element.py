lst=[10,11,12,13,14]

num=int(input("Enter the number you want to check in the list"))
flag=0

for i in lst:
    if i==num:
        flag=0
        break
    elif i!=num:
        flag=1
if flag==0:
    print("The number exists in the list")

if flag==1:
    print("Number not exist")




