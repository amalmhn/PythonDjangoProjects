num=10 #global scope
def changer():
    global num #making the num variable globally
    num=20 #local scope
    print(num)

changer()
print(num)

#--HW--
#implmtn stack data structure using list