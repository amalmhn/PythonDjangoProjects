#??create a stuednt class consist of attributes roll number name course total
#??must have methods for setting this attributes(set and print)

class Student:
    def set_student(self,roll,name,course,total):
        #the below are called 'instance variables' (self should be there)
        self.roll = roll
        self.name = name
        self.course = course
        self.total = total

    def print_student(self):
        print('roll',self.roll)
        print('name',self.name)
        print('course',self.course)
        print('total',self.total)

obj=Student()
obj.set_student(111,'Amal','dev',100)
obj.print_student()

#we can acces insctance variables outside the class by using reference
print(obj.name)
#you can replace the name roll course. Details in screenshot taken on 9/12/2020


