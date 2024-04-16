#!/usr/bin/python3
"""
A custom list class that inherits from the built-in list class.
"""

class MyList(list):
    """
    A custom list class that provides additional functionality.
    """

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)

