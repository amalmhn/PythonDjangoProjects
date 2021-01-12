# def sub(num1,num2):
#     return num1-num2

def sub_dec(func):
    def wrap(no1,no2): #to change the values in a defined fnctn
        if no1<no2:
            no1,no2=no2,no1
        return func(no1,no2)
    return wrap

@sub_dec #decorator
def sub(num1,num2):
    return num1-num2

res=sub(40,50)
print(res)