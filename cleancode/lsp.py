
from abc import ABC, abstractmethod

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#     def __setattr__(self, key, value):
#         super().__setattr__(key, value)
#         if key in ("width", "height"):
#             self.__dict__["width"] = value
#             self.__dict__["height"] = value
#
# rect = Rectangle(5,6)
# print(rect.calculate_area())  # Outputs: 30
#
# rect.width = 7
# print(rect.calculate_area())  # Outputs: 42
#
# sqr = Square(5)
# print(sqr.calculate_area())  # Outputs: 25
#
# sqr.width = 7
# print(sqr.calculate_area())  # Outputs: 49


# The 'Square' subclass is defined in a way that width always equals height. Now, this would be a violation of LSP
# if your program expects instances of Rectangle and Square to allow independent modification of width and height;
# when you try to change width of the 'square', the height changes too, which wouldn't be expected if this is meant to be a 'Rectangle'.


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

print(Rectangle(10, 5).calculate_area())
print(Square(5).calculate_area())