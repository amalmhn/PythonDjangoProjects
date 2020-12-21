bdaydate=input("ente your bday dd-mm-yyyy")
cudate=input("enter currentdate dd-mm-yyyy")


print(bdaydate)#20-11-2020
print(cudate)#18-11-2020

bdate,bmonth,byear=bdaydate.split("-")#20-11-2019
cdate,cmonth,cyear=cudate.split("-")#18-11-2020

age=int(cyear)-int(byear) #1

if(cmonth<=bmonth): #11<=11
    if(cdate<bdate): #18<20
        age-=1#age=0
print("you are ",age,"years old")