#exception
#exception and error are NOT the same
#abnormal code that disrupt our normal execution

no1=int(input('num1'))
no2=int(input('num2'))
lst=[1,2,3]
try:#doubtful code
    res=no1/no2
    print(res)
    print("I have data base")
# except:#corresponding exception
#     print('Exception occured')

except Exception as e: #to get system error msg
    print(e.args)

try:
    print(lst[5])
except Exception as e:
    print(e.args)


#you can give unlilimited try in program