from dbconnectpgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
sql='select * from faculty'

try:
    cursor.execute(sql)
    queryset=cursor.fetchall()
    for faculty in queryset: #to get particular values
        print(faculty)
except Exception as e:
    print(e.args)
finally:db.close()