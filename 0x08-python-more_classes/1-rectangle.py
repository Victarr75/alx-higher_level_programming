#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        # Initialize the Rectangle object with optional width and height
        self.width = width  # Set the width using the property setter method
        self.height = height  # Set the height using the property setter method

    @property
    def width(self):
        # Getter method for retrieving the width attribute
        return self.__width

    @width.setter
    def width(self, value):
        # Setter method for setting the width attribute
        if not isinstance(value, int):  # Check if the value is an integer
            raise TypeError("width must be an integer")  # Raise TypeError if not
        elif value < 0:  # Check if the value is less than 0
            raise ValueError("width must be >= 0")  # Raise ValueError if less than 0
        else:
            self.__width = value  # Set the width attribute

    @property
    def height(self):
        # Getter method for retrieving the height attribute
        return self.__height

    @height.setter
    def height(self, value):
        # Setter method for setting the height attribute
        if not isinstance(value, int):  # Check if the value is an integer
            raise TypeError("height must be an integer")  # Raise TypeError if not
        elif value < 0:  # Check if the value is less than 0
            raise ValueError("height must be >= 0")  # Raise ValueError if less than 0
        else:
            self.__height = value  # Set the height attribute
