#Create a class Student with attributes name, roll_number, and grade.

# Add a method to update the student's grade.           
"""doubt"""
# Create a few Student objects and demonstrate updating their grades.

class Student:
    def __init__(self, name,roll_no, grade):
        self.name=name
        self.roll_no=roll_no
        self.grade=grade
    def upgrade_grade(self, new_grade):
        self.grade=new_grade
        
    def info(self):
        print(self.name, self.grade,self.roll_no)
obj1= Student("Saksham", 1, "A")
obj1.upgrade_grade("B")
obj1.info()
