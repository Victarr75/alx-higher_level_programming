#!/usr/bin/python3

import random

# Generate a random number between -10000 and 10000
number = random.randint(-10000, 10000)

# Calculate the last digit of the absolute value of the number
last_digit = abs(number) % 10

# Check conditions and print corresponding messages
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit))
else:
    print("Last digit of {} is 0 and is 0".format(number))
