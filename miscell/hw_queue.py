import queue
size=int(input('Enter the size of the queue'))
Q=queue.Queue(maxsize=size)
n=1
top=0

def Q_put():
    global top
    if top==size:
        print('The queue is full')
    else:
        element=int(input("Enter the element"))
        Q.put(element)
        top+=1
def Q_get():
    global top
    if top==0:
        print("The queue is empty")
    else:
        Q.get()
        top-=1
def Q_disp():
    print('The queue is',list(Q.queue))
while (n!=0):
    option=int(input('ENTER THE OPTION \n 1)Add element\n'
                     ' 2)Remove element\n 3)Display the queue'))
    if option==1:
        # element=int(input('Enter the element'))
        Q_put()
    elif option==2:
        Q_get()
    elif option==3:
        Q_disp()
    n=int(input('Press "1" for continue and "0" for exit'))