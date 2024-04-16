#!/usr/bin/python3
"""
Rectangle module containing the Rectangle class.
"""

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
