from Circle import Circle
from Rectangle import Rectangle
from JSONR import jsoncreator
from Excel import exceler

newCircle = Circle(8)
print(newCircle.area())
print(newCircle.circumference())

newRectangle = Rectangle(12,10)
print(newRectangle.rectangle_area())

#newJSON = jsoncreator()
#newJSON.create_json()

newExcel = exceler()
print(newExcel.find_date('employee.xlsx'))
print(newExcel.sort_dates('employee.xlsx'))