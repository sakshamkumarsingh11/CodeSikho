

#repr method

class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f"Name of student {self.name} and age is {self.age}" 

s1= Student("Saksham",18)
print(repr(s1))



#__cmp__method



class Student:
    def __init__(self, age):
        self.age=age
    def __cmp__(self,other):
        if self.age> other.age:
            return 1
        elif self.age<other.age:
            return-1
        else:
            return 0
    
s1=Student(15)                                                                              #doubt
s2=Student(12)


print(cmp(s1, s2)) 


#__call__() method


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
print(double(5))

