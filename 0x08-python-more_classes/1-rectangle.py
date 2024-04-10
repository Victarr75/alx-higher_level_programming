#!/usr/bin/python3
"""This is a Rectangle class"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle object with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for retrieving the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for setting the width attribute"""
        if not isinstance(value, int):  
            raise TypeError("width must be an integer")
        elif value < 0:  
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for retrieving the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for setting the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
