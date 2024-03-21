#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """ returns a set of all elements
    present in only each of the sets.
    """
    return (set_1 ^ set_2)
