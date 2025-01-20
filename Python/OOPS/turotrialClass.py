class Account_holder:
    def __init__(self, name, account_no, balance):
        self.name=name
        self.account_no=account_no
        self. balance=balance
    def info(self):
        print(f"Name of the account holder is {self.name} and the acoount number {self.account_no} with balance {self.balance}")

obj1=Account_holder ("Pratyush", "S24cse1", 100000)
obj1.info()
obj2= Account_holder("Harshit", "S24cse2", 10)
obj2.info()