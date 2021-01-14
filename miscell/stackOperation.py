size=int(input('Enter the size of the stack'))
stk=[]
top=0
n=1
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
    print(top)
    if top<=0:
        print('Stack is empty')
    else:
        print(stk[top-1],'popped')
        top-=1

def display():
    global top
    for i in range(0,top):
        print(stk[i])
    print('display...')

while(n!=0):
    option=int(input("Enter operation you want to perform 1)push 2)pop 3)display"))
    if option==1:
        element=input('Enter the element')
        push(element)
    elif option==2:
        pop()
    elif option==3:
        display()
    else:
        print('invalid option')
    n=int(input('If you want to continue press "1" , Press 0 for exit'))



#HW_Queue
# ------
# fifo
# insert
# delete
#       r
# queu=[][][][]
#       f

# datasructure
# types of data structure
