# Define a class named Rectangle which can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def find_area(self):
        area = self.length * self.width
        return area


rectangle_1 = Rectangle(5, 4)
print(rectangle_1.find_area())
