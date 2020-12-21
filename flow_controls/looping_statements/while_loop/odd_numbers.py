low=int(input("Enter the lower limit"))
upper=int(input("Enter the upper limit"))
sum=0
if (low>upper):
    print("error")
while(low<=upper):
    if(low%2!=0):
        sum+=low
    low+=1

print(sum)

