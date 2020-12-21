lst=[2,1,3,4,6,7]

lst.sort() #this is a method
# sorted(lst) this is a function

low=0
upper=len(lst)-1
element=int(input("enter an element"))
while (low<upper):
    total=lst[low]+lst[upper]
    if (element<total):
        upper=upper-1

    elif (element>total):
        low=low+1

    elif (element==total):
        print("pairs are", lst[low],'and', lst[upper])
        break



