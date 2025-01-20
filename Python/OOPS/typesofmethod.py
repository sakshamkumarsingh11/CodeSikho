"""Types of methods
1-instance
2-class
3-static"""

# for understanding.... static variable ko easily bana sakte hai bs instance ke bahar bana ke 
"""eg- 
class student:

    school=abc
    def__init__(self......)...."""
    
    #instance method
class Student():
    def __init__(self,name, section):
        self.name=name
        self.section=section
    def display(self):
        print(f" My name is {self.name} and i study in section{self.section}")
    
obj1= Student("Saksham", "cse")
obj1.display()



"""yaha pe  pehle obj define  kiya fir method call kiya object ke sath"""



            #class method
            
            
class Rectangle:
    def __init__(self, l, b):
        self.l=l
        self.b=b
    def area(self):
        return  self.l*self.b
    """yaha tak normal isntance ki tarah use kiya ha ab aega class method"""
    @classmethod
    def square(cls, side):             #new argument. used in classmethdos
        return cls(side,side)
    
s = Rectangle.square(15)            # called the class and the method required direct and assigned the value
print( s.area())

#Yaha pe yeh nhi kiya ha s1=rectangle("xyz") then s1.method_name
        #yaha pe sida s=class_name.method_name(argument)




            # static method
            
#no argument is used 

class TempConverter:
    @staticmethod
    def CtoF(C):
        return 9* C/5+32
    @staticmethod
    def FtoC(F):
        return 5* (F-32)/ 9

f=TempConverter.CtoF(15)
print (f)

"""Isme bhi same class method ki tarah class call hua fir method bs koi argument nhi pas kiya"""