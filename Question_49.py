# Define a class named Shape and its subclass Square. The Square class has 
# an init function which takes a length as argument. Both classes have 
# a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, a=0):
        self.a = a

    def area(self):
        sq_area = self.a**2
        return sq_area


sqr_1 = Square(4)
print(sqr_1.area())

print(Square().area())
