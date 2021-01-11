import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    database='demo',
    passwd='Password@123'
)
cursor=db.cursor()

id=input("Enter the id no.")
name=input('Enter the name')
subject=input('Enter the subject')



# sql=('insert into faculty(id,name,subject) values(%s,%s,%s)',(id,name,subject))

try:
    cursor.execute('insert into faculty(id,name,subject) values(%s,%s,%s)',(id,name,subject))
    db.commit()
    print("sucess")
except Exception as e:
    print(e.args)
finally:
    db.close()

