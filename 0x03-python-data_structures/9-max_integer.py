#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    max_val = my_list[0]  # Assume the first element as the maximum initially
    for num in my_list:
        if num > max_val:
            max_val = num  # Update max_val if a larger number is found

    return max_val
        

