#inheritance
#parent     base        sueper class
#child      derived     sub class

class Parent:
    def phone(self):
        print('have Nokia 5310')

    def lap_top(self):
        print("I have laptop")

class Child(Parent): #child extends parent here. INHERITANCE
    def bike(self):
        print('I have bike')

ch=Child() #shorting the class name (REFERENCE)
ch.phone()
ch.bike() #ch can access both parent and child functions

