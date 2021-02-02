import math
class Circle():
    
     def __init__(self,radius):
         self.radius = radius
     def area(self):
         area = math.pi * (self.radius)**2
         return area
     def circumference(self):
       
         circumference = 2* math.pi * self.radius
         return circumference
