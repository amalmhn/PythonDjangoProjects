import mysql.connector
db=mysql.connector.connect( #step 2
    host='localhost',
    user='root',
    passwd='Password@123'
)
#step3
cursor=db.cursor()