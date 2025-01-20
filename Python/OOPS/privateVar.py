class Numbers:
    def __init__(self, variable1, variable2):
        self.variable1=variable1
        self.__variable2=variable2
    def display(self):
        print(f"variable number one is {self.variable1}")
        print(f"variable number two is {self.variable2}")

obj1= Numbers(15,13)
obj2= Numbers(22,21)

obj1.display()
obj2.display()



#Here the variable2 is been private and could not perfom any method here.





#real life example-
"""class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.__check_funds(amount):  # Calling a private method
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    def __check_funds(self, amount):  # Private method
        return self.balance >= amount
"""