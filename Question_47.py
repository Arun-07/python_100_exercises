# Define a class named Circle which can be constructed by a radius. 
# The Circle class has a method which can compute the area.

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)

    def find_area(self):
        a = (22/7)* self.radius**2
        return round(float(a),2)


circle_1 = Circle(5)

print(circle_1.find_area())
