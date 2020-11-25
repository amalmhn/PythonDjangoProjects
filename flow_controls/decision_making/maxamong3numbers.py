num1=int(input('Enter 1st number'))
num2=int(input('Enter 2nd number'))
num3=int(input('Enter 3rd number'))

if((num1>num2)&(num1>num3)):
    print('num1 is greatest')
    if(num2>num3):
        print('Second largest number is num2')
    else:
        print('Second largest number is num3')
elif((num2>num1)&(num2>num3)):
    print('num2 is greatest')
    if (num3 > num1):
        print('Second largest number is num3')
    else:
        print('Second largest number is num1')
elif((num3>num1)&(num3>num2)):
    print('num3 is greatest')
    if (num2 > num1):
        print('Second largest number is num2')
    else:
        print('Second largest number is num1')
else:
    print('Numbers are equal')
