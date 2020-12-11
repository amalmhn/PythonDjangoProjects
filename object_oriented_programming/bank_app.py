class Bank:

    bank_name="SBK" #static variable
    @staticmethod #decorator
    def utility_method():
        print('utility method')
    @classmethod
    def change_bank_name(cls):
        cls.bank_name='SBK'

    def create_account(self,acno,name,balance): #instance method
        self.acno=acno
        self.name=name
        self.balance=balance


    def deposit(self,amount):
        self.balance+=amount
        #accessing the static variable below "Bank.bank_name"
        print(Bank.bank_name,"your acccount",self.acno,'has been credited with the amount',amount,
              'your balance is ',self.balance)


    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance in you",self.acno,'transaction declined')
        else:
            self.balance-=amount
            print('your account',self.acno,'has been debited with the amount',amount,
                  'your available balance is',self.balance)

    def balance_enq(self):
        print('your available balance is',self.balance)

obj=Bank()
obj.create_account(1001,'Amal',5000)
obj.deposit(5000)
obj.withdraw(1000)
obj.balance_enq()

#how to acces instance variables outside the class
print(obj.acno)

#static method
Bank.utility_method()

