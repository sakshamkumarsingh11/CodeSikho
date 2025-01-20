class Student:
    def __init__ (self, name):
        self.name=name
        print(f"Student {self.name} is invited")
    def __del__ (self):
        print(f"The name of student who left is {self.name}")
    
s1=Student("Ajay")

s2=Student("Vijay")
del s1



"""doubt"""
