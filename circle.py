
import math
from shape import Shape


# The Circle class is a subclass of the Shape class and provides static methods to calculate the area
# and perimeter of a circle given its radius.
class Circle(Shape):
    """
    The above function calculates the area of a circle given its radius.
    
    :param radius: The radius is a parameter that represents the length from the center of a circle
    to any point on its circumference
    :return: The area of a circle with the given radius.
    """
    @staticmethod
    def calculateArea(radius):
        return math.pi * radius ** 2
    

    """
    The above function calculates the perimeter of a circle given its radius.
    
    :param radius: The radius of a circle
    :return: The perimeter of a circle with the given radius.
    """
    @staticmethod
    def calculatePerimeter(radius):
        return 2 * math.pi * radius