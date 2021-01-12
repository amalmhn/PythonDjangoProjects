from tkinter import *
root=Tk()
import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    database='demo',
    passwd='Password@123'
)

cursor=db.cursor()

# id=input("Enter your student ID number")
# name=input("Enter your Name")
# course=input("Enter your course name")


def save_button():
    id_no=uentry.get()
    name_student=mentry.get()
    course_student=loentry.get()

    try:
        cursor.execute('insert into registration(ID,Name,Course)values(%s,%s,%s)',(id_no,name_student,
                                                                                    course_student))
        db.commit()
        print('Successfully registered')
    except Exception as e:
        print(e.args)
    finally:
        db.close()

ulabel=Label(root,text='ID NO.')
mlabel=Label(root,text='Name')
lolabel=Label(root,text='Course')

uentry=Entry(root)
mentry=Entry(root)
loentry=Entry(root)

ulabel.grid(row=0,column=0)
mlabel.grid(row=1,column=0)
lolabel.grid(row=2,column=0)

uentry.grid(row=0,column=2)
mentry.grid(row=1,column=2)
loentry.grid(row=2,column=2)

btn=Button(root,text='Save',command=save_button)
btn.grid(row=3,column=2)

root.mainloop()