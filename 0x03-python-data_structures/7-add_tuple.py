#!/usr/bin/python
def add_tuple(tuple_a=(), tuple_b=()):
     x1 = x2 = y1 = y2 = 0

    if len(tuple_a) >= 2:
        x1 = tuple_a[0]
        x2 = tuple_a[1]
    elif len(tuple_a) == 1:
        x1 = tuple_a[0]

    if len(tuple_b) >= 2:
        y1 = tuple_b[0]
        y2 = tuple_b[1]
    elif len(tuple_b) == 1:
        y1 = tuple_b[0]

    return (x1 + y1, x2 + y2)
