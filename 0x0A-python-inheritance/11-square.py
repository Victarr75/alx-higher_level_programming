#!/usr/bin/python3
"""
Square module containing the Square class.
"""

class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size.
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the string representation of the Square.
        """
        return f"[Square] {self.__size}/{self.__size}"

