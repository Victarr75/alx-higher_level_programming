#!/usr/bin/python3
def best_score(a_dictionary):
    """returns the value of the best score
    """
    if a_dictionary is None:
        return None
    best_key = None
    best_score = 0
    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            best_key = key
    return best_key
