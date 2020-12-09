class Bank:


    def create_account(self,acno,name,balance,bank_name):
        self.acno=acno
        self.name=name
        self.balance=balance
        self.bank_name=bank_name

    def deposit(self,amount):
        self.balance+=amount
        print("your acccount",self.acno,'has been credited with the amount',amount,
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
obj.create_account(1001,'Amal',5000,'SBK')
obj.deposit(5000)
obj.withdraw(1000)
obj.balance_enq()

