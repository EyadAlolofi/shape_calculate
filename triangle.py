

import math
from shape import Shape


# The Triangle class calculates the area and perimeter of a triangle given the lengths of its sides.
class Triangle(Shape):

    """
    The function calculates the area of a triangle using the lengths of its sides.
    
    :param side1: The length of the first side of the triangle
    :param side2: The parameter "side2" represents the length of the second side of a triangle
    :param side3: The length of the third side of the triangle
    :return: the area of a triangle.
    """
    @staticmethod
    def calculateArea(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))



    """
    This function calculates the perimeter of a triangle given the lengths of its three sides.
    
    :param side1: The length of the first side of the triangle
    :param side2: The parameter "side2" represents the length of the second side of a triangle
    :param side3: The third side of a triangle
    :return: The sum of side1, side2, and side3.
    """
    @staticmethod
    def calculatePerimeter(side1, side2, side3):
        return side1 + side2 + side3
    

    