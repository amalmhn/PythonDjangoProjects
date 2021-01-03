# #age<18
#
# age=int(input('Enter the age'))
#
# if age<18:
#     raise Exception("Sorry Invalid age") #customized exception aka
#                                             #customized system error msg
#                                         #for this we are using 'throw' kywrd in JAVA
#
#


num=input("ENter an integer")

if type(num)!='int':
    raise Exception("Invalid")