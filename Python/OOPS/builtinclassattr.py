"""1) __dict___"""

class Car:
    wheels = 4  # Class attribute

    def __init__(self, make, model):
        self.make = make    # Instance attribute
        self.model = model  # Instance attribute

# Accessing __dict__ on an instance
my_car = Car("Toyota", "Camry")
print(my_car.__dict__)
# Output: {'make': 'Toyota', 'model': 'Camry'}

# Accessing __dict__ on a class
print(Car.__dict__)
# Output: {'wheels': 4, '__module__': '__main__', '__init__': <function ...>, ...}





"""2) __class__"""


my_car = Car("Toyota", "Camry")
print(my_car.__class__)  # Output: <class '__main__.Car'>







"""3)__name__"""
print(Car.__name__)  # Output: Car







"""4) __module__"""
print(Car.__module__)  # Output: __main__







"""5)__bases__"""
class Vehicle:
    pass
class Car(Vehicle):
    pass
print(Car.__bases__)  # Output: (<class '__main__.Vehicle'>,)
# can be used to find parent class or base class in case of inheritence 





"""6)__doc__"""

class Car:
    """This class represents a car object with make and model."""

print(Car.__doc__)  # Output: This class represents a car object with make and model.




"""7)__annotations__"""

class Car:
    make: str
    model: str

print(Car.__annotations__)  # Output: {'make': <class 'str'>, 'model': <class 'str'>}
