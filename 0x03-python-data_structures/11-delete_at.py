#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # Initialize an empty list to store the modified list
    new_list = []

    # Iterate over the original list
    for i in range(len(my_list)):
        # Append elements to the new list except the one at idx
        if i != idx:
            new_list.append(my_list[i])
    
    return new_list
