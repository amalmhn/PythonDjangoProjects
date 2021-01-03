no1=int(input("Enter num1"))
no2=int(input('Enter num2'))

try:
    res=no1/no2
    print(res)

except:
    if no2==0:
        raise Exception ('You cant use zero')