from dbconnectpgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
sql='insert into faculty(id,name,subject)values("100","ajay","datastructure")'

try:
    cursor.execute(sql)
    db.commit() #telling to reflect those changes like inserting the values to table
    print('query executed')
except Exception as e:
    print(e.args)
finally:
    db.close()