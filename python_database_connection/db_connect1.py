#1.import mysql package
#2.establish connection mysql -u root -p
#3.curser object (to move data in and out)
#4.excecute queries
#5.close databse connection

import mysql.connector
db=mysql.connector.connect( #step 2
    host='localhost',
    user='root',
    passwd='Password@123'
)
#step3
cursor=db.cursor()

sql='SELECT VERSION()' #query

cursor.execute(sql)
data=cursor.fetchone()
print(data)
