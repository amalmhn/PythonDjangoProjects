# def add(num1,num2):
#     res=num1+num2
#     print(res)
#
# add(10,20)

#variable length argument methods

def add(*args): # "*" will help to input infinite arguments
    total=0
    for num in args:
        total+=num
    print(total)  #values will accpet as tuple


add(10,20)
add(10,20,30)
add(10,11,12,13,14)

print('---------------------------------------------------------------')


def printEmp(**arg):  # "*" will help to input infinite arguments into dict
    print(arg)  #values will accpet as dict
printEmp(Home='Kakkanad',Name="Ajay",Working='aluway')


# *arg accpests in tuple format and **args accept in dict format

