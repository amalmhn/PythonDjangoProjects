num1=int(input('Enter 1st number'))
num2=int(input('Enter 2nd number'))
num3=int(input('Enter 3rd number'))

if((num1>num2)&(num1>num3)):

    if(num2>num3):
        print(num1,num2,num3)
    elif(num3>num2):
        print(num1, num3, num2)

elif((num2>num1)&(num2>num3)):

    if(num1>num3):
        print(num2,num1,num3)
    elif(num3>num1):
        print(num2, num3, num1)

elif((num3>num2)&(num3>num1)):

    if(num2>num1):
        print(num3,num2,num1)
    elif(num1>num2):
        print(num3, num1, num2)

else:
    print('All numbers are same')


# elif((num2>num1)&(num2>num3)):
#     print(num2)
#     if (num3 > num1):
#         print(num3 , num1)

#         print(num1)
#     elif(num1>num3):
#         print()
# elif((num3>num1)&(num3>num2)):
#     print(num3)
#     if (num2 > num1):
#         print(num2)
#
#         print(num1)
# else:
#     print('Numbers are equal')

