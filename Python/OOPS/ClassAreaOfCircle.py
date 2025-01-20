class circle:
    radius=7
    r=radius**2
    def area(self):
        area= 3.14*self.r
        return area
        
obj = circle()
print(obj.area())