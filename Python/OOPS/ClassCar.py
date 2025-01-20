class Car:
    def __init__(self,brand,model,year):
        
        self.brand= brand
        self.model=model
        self.year=year
    
    def info(self):
        print(f"The car is {self.brand} {self.model} of year{self.year}")
my_car=Car ("audi","q4",2020)
my_car.info()

