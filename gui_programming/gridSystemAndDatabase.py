from tkinter import *
root=Tk()

import mysql.connector
from dbconnectpgm.dbconnect import *

def db_connect(uername,password):
    #db connect logic
    print('inside..........')
    db=get_connection()
    cursor=db.cursor()
    try:
        cursor.execute('select * from userr where username=%s and password=%s',(uername ,password))
        user=cursor.fetchone()
        print(user)
        id='1001'
        name='test1'
        usertest='test1'
        userpwd='test2'
        sql='insert into userr(id,name,username,password)values("%s","%s","%s","%s")'%\
            (id,name,usertest,userpwd)
        cursor.execute(sql)
        db.commit()

    except Exception as e:
        print(e.args)
def authenticate_user():
    uname=uentry.get()
    pwd=pentry.get()
    db_connect(uname,pwd)

ulabel=Label(root,text='username')
plabel=Label(root,text='password')
uentry=Entry(root)
pentry=Entry(root)

btn=Button(root,text='login',command=authenticate_user)
ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)

uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)
btn.grid(row=2,column=1)
root.mainloop()