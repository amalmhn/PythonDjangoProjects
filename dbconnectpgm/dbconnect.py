import mysql.connector

def get_connection():
    db=mysql.connector.connect( #step 2
        host='localhost',
        user='root',
        database='demo', #already available database
        passwd='Password@123'
    )
    return db
#step3
