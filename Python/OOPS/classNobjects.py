class Bank_account:
    def __init__(self, account_number, balance=0):
        self.account_number= account_number
        self.balance=balance
    
    def deposit(self, deposit1):
        if deposit1>0:
            self.balance+=deposit1
            print(f"The balance is: {self.balance}")
        else:
          print("The deposit amount must be positive")

    def withdrawl(self,withdrawl):
        if withdrawl< self.balance:
            self.balance-=withdrawl
            print (f"The balance is: {self.balance}")
        else:
            print("Insufficient amount in the balance")

my_accountnumber= Bank_account("12345")
my_accountnumber.deposit(15000)
my_accountnumber.withdrawl(10000)
my_accountnumber.withdrawl(2000000)