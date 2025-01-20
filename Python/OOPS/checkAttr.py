# 1 hasattr()
class Car:
    def __init__(self, make):
        self.make = make

my_car = Car("Toyota")
print(hasattr(my_car, "make"))    # Output: True
print(hasattr(my_car, "model"))   # Output: False




#2 getattr()

class Car:
    def __init__(self, make):
        self.make = make

my_car = Car("Toyota")
print(getattr(my_car, "make"))          # Output: Toyota
print(getattr(my_car, "model", "N/A"))  # Output: N/A (since "model" doesn't exist)




# 3 setattr
class Car:
    def __init__(self, make):
        self.make = make

my_car = Car("Toyota")
setattr(my_car, "model", "Camry")  # Creates a new attribute "model"
print(my_car.model)                # Output: Camry

setattr(my_car, "make", "Honda")   # Updates the "make" attribute
print(my_car.make)                 # Output: Honda


# delattr()
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Camry")
print(my_car.model)       # Output: Camry

delattr(my_car, "model")  # Deletes the "model" attribute
# print(my_car.model)     # This would raise an AttributeError since "model" no longer exists
