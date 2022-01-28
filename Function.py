#!/usr/bin/env python

"""Loop.py: Demo code for python functions"""

__author__ = "Sumit Kala"


def void_function(n=5):  # default value
    print("value of n = ", n)


def return_function(n=5):  # default value
    print("value of n = ", n)
    return n * n


def main():
    x = void_function()
    print(x)
    x = return_function(10)
    print(x)


if __name__ == '__main__': # forces the interpreter to read the complete file before execution
    main()
