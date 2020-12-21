class Maths:
    def add(self):
        print('inside no arg add method')

    def add(self,num1):
        print('inside single arg add method')

    def add(self,num1,num2): #the receiving values called parameters
        print('inside two arg add method')


#here same method name, different number of arguments.
#add()

m=Maths()

m.add(10,20) #This passing values are variables
m.add(10)

#in python recently implemented method will work. ie method overloading

#if this overloading outside a class, called function overloading