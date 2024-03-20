#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 argument{}.".format('.' if len(sys.argv) == 1 else ''))
    else:
        print("{} argument{}:".format(len(sys.argv) - 1, 's' if len(sys.argv) > 2 else ''))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))

