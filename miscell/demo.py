size=int(input("Enter the size of the stack"))
stk=[]
top=0
n=1.

def push(element):
    global top
    if top>=size:
        print('stack is full')
    else:
        stk.insert(top,element)
        print('Element pushed')
        top+=1
        print('Top is now',top)
def pop():
    global top
    if top<=0:
        print('Stack is empty')
    else:
        print(stk[top-1],'popped')
        top-=1
def display():
    global top
    for i in range(0,top):
        print(stk[i])

while n!=0:
    option=int(input('Enter operation you want to perform 1)Push 2)Pop 3)Display'))
    if option==1:
        element=int(input('Enter the element'))
        push(element)
    elif option==2:
        pop()
    elif option==3:
        display()
    else:
        print('Invalid option')
    n=int(input('Press "1" for continue, "0" for exit'))