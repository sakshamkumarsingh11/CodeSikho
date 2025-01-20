class Employee:
    def __init__ (self,name,id_no):
        self.name=name
        self.id_no=id_no
    def info(self):
         print(f"The user is {self.name} with id {self.id_no}")
class Programmer(Employee):
    def about(self):
        print(f"{self.name} is also a programmer")
e1 = Employee ("Saksham",112)
e1.info()

e2 = Programmer("Xyz",911)
e2.about()
e2.info()