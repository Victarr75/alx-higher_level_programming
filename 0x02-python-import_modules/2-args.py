#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args_count = len(sys.argv) - 1
    if args_count == 0:
        print("0 argument{}.".format('.' if args_count == 0 else ''))
    else:
        print("{} argument{}:".format(args_count, 's' if args_count > 1 else ''))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
