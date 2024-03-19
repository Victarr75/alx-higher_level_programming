#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Reverse the list in place
    my_list.reverse()
    
    # Iterate through the reversed list
    for i in my_list:
        # Print each integer using str.format()
        print("{:d}".format(i))
