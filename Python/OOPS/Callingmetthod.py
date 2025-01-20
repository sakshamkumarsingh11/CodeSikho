#CALLING A CLASS METHOD FROM ANOTHER CLASS METHOD
#Program to call a class method from another class method



class ABC():
    def __init__(self, var):
        self.var=var
    def display(self):
        print(f"variable is {self.var}")
    def add_2(self):
        self.var+=2
        self.display()                  #called class method here in another class method
obj= ABC(12)
obj.add_2()


#PROGRAM TO SHOW HOW A CLASS METHOD CALLS A FUNCTION DEFINED IN GLOBAL NAMESPACE


def multiplier_10(x):
    return x*10

class Number():
    def __init__(self, num):
        self.num=naum
    def display(self):
        print(f"the number is {self.num}")
    def modify(self):
        self.variable=multiplier_10(self.num)
        
obj = Number(10)
obj.display()
obj.modify()
obj.display()


