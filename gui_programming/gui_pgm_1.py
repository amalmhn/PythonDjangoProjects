from tkinter import *
#variable
root=Tk()
root.title('Main window')
label1=Label(root,text='username')
label2=Label(root,text='email address')
label3=Label(root,text='password')
entry1=Entry(root)

label1.pack() #to view the label inside the window
entry1.pack()
label2.pack()
label3.pack()

root.mainloop()