#!/usr/bin/python3
def no_c(my_string):
    g_string = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            g_string += my_string[i]
    return (g_string)
