#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a is smaller than 2, fill missing integers with 0
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    
    # If tuple_b is smaller than 2, fill missing integers with 0
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    
    # Take only the first 2 integers of each tuple
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
    
    # Add corresponding elements and return the result as a tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

