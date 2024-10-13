# polymorphism_demo.py

import math

# Base Class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override this method")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(5, 3)
    circle = Circle(4)

    print("Area of Rectangle:", rectangle.area())
    print("Area of Circle:", circle.area())
