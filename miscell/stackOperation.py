size=int(input('Enter the size of the stack'))
stk=[size]

top=0
n=1
def push():
    global top
    if top>=size:
        print('stack is full')
    else:
        stk.append(element)
        top+=1

def pop():
    print('pop...')
def display():
    print('display...')

while(n!=0):
    option=int(input("Enter operation you want to perform 1)push 2)pop 3)display"))
    if option==1:
        element=input('Enter the number')
        push(element)
    elif option==2:
        pop()
    elif option==3:
        display()
    else:
        print('invalid option')
    n=int(input('If you want to continue press "1" , Press 0 for exit'))
