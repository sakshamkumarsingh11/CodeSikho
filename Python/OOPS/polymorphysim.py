"""class Student:
    def display(self, name=''):
        print(f"Hello world, {name}")

obj=Student()
obj.display()
obj.display("SKS")
"""

#yaha pe kya hua ki name nam seh ek argument toh pass kr diya with empty output, yaha pe name diya toh name aya vrna blank output jaega



class Student:
    def display (self):
        print("Hello world")
    
class Child(Student):
    def display(self):          #same name methods
        super().display()
        print("Observe the function name")

obj=Child()
obj.display()           #now it only take the method under child, to use the parent class method we use ""Super9)""

