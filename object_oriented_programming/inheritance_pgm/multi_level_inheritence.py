class Parent:
    def m1(self):
        print("print inside parent")


class Child(Parent):
    def m2(self):
        print("print inside child")

class SubChild(Child):
    def m3(self):
        print('print inside subchild')
#MULTIPLE INHERITANCE
# class SubChild(Child,Parent):
#     def m3(self):
#         print('print inside subchild')

sb=SubChild()
sb.m3()
sb.m2()
sb.m1()

ch=Child()
ch.m2()
ch.m1()

p=Parent()
p.m1()

