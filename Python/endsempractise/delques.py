class Car:
    def __init__(self, model):
        self.model=model
    
    def display (self):
        print(f"Model: {self.model}")
    def __del__(self):
        print(f" Model")
car1=Car("Mercedes gls")
car1.display()
del car1