"""class Student:

    def __init__ (self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        
    def display(self):
        print(f"My name is{self.name} and roll_no is{self.roll_no}")
        
obj=Student("saksham", "1234")
obj.display()"""



class Student:
    def __init__(self,name,maths,english,science):
        self.name=name
        self.english=english
        self.maths=maths
        self.science=science
    def display(self):
        print(F"Name of the student is {self.name}. Number obtained in english, maths and science  are {self.maths}, {self.english} and {self.science} respectively")
    
    def average(self):
        return (self.maths+self.science+self.english)/3
s1=Student("Saksham", 90,95,85)
s1.display()
s1.average()


#class variable and object variable
"""

class Student:
college_name=bennett            #class_variable

    def __init__(self,name,maths,english,science):
        self.name=name                  #object variable
        self.english=english
        self.maths=maths
        self.science=science
    def display(self):
        print(F"Name of the student is {self.name}. Number obtained in english, maths and science  are {self.maths}, {self.english} and {self.science} respectively")
    
    def average(self):
        return (self.maths+self.science+self.english)/3
s1=Student("Saksham", 90,95,85)
s1.display()
s1.average()"""