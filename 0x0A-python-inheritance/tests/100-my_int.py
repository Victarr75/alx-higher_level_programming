#!/usr/bin/python3
"""
MyInt module containing the MyInt class.
"""

class MyInt(int):
    """
    A class representing an integer with inverted equality operators.
    """

    def __eq__(self, other):
        """
        Overrides the == operator to behave as !=.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to behave as ==.
        """
        return super().__eq__(other)

