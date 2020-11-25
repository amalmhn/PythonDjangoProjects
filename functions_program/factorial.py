#create a function to perform factorial of a number


#function with argument and no return value
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(fact)

fact(4)

#function with argument and with  return value
def add(num1,num2):
    res=num1+num2
    return res
data=add(150,150)
print(data)
