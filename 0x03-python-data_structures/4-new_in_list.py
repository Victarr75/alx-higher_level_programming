#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if the index is within the bounds of the list
    if idx < 0 or idx >= len(my_list):
        return my_list  # If index is out of bounds, return the original list
    
    # Create a copy of the original list
    new_list = list(my_list)
    
    # Replace the element at the specified index with the new element
    new_list[idx] = element
    
    return new_list  # Return the modified list
