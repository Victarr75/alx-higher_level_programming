#!/bin/bash/python3
import sys


def print_arguments():
    num_args = len(sys.argv) - 1
    print(f"Number of argument{'s' if num_args !=
          1 else ''}: {num_args}", end='')
    if num_args == 0:
        print(".")
    else:
        print(":")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments()
