#!/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("Cannot dynamically create new instance attributes")
        self.__dict__[name] = value
