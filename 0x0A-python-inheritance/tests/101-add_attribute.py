#!/usr/bin/python3
"""
Module containing a function to add a new attribute to an object.
"""

def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.
    Raises a TypeError if the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

