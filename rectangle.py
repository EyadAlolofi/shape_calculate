import math
from shape import Shape

# The Rectangle class calculates the area and perimeter of a rectangle given its length and width.
class Rectangle(Shape):

    """
        The function calculates the area of a rectangle given its length and width.
        
        :param length: The length of the rectangle
        :param width: The width is a measurement of the horizontal distance of an object or space. It is
        typically measured in units such as inches, centimeters, or meters
        :return: the product of the length and width, which represents the area of a rectangle.
        """
    @staticmethod
    def calculateArea(length, width):
        
        return length * width


    """
    The function calculates the perimeter of a rectangle given its length and width.
    
    :param length: The length of a rectangle or a square
    :param width: The width of the rectangle
    :return: the calculated perimeter of a rectangle.
    """
    @staticmethod
    def calculatePerimeter(length, width):
        
        return 2 * (length + width)