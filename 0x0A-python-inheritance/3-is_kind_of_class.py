#!/usr/bin/python3
"""
Checks if an object is an instance of, or if it inherits from, the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if it inherits from,
    the specified class; otherwise False.
    """
    return isinstance(obj, a_class)

