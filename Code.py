from Rectangle import Rectangle
from Circle import Circle
from JSON import JSON
import math
newRectangle = Rectangle(12,10)
print(newRectangle.rectangle_area())

NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.circumference())

newJSON = JSON()
newJSON.create_json()