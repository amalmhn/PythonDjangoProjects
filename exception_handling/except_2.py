no1=int(input('no1'))
no2=int(input('no2'))

try:
    res=no1/no2
    print(res)
except:
    no2=int(input('New value for no2'))
    try:
        res = no1 / no2
        print(res)
    except:
        no2 = int(input('New value for no2'))

finally: #this will run even if an error in try and except  
    print('I have database transcation')
    print('I have one file transaction')


#PYTHON TO MYSQL
# import package
# establish connection
# create curser object
# execute queries exception
# close connection


#try: abnormal code
# exec
