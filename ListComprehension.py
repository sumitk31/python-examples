#!/usr/bin/env python

"""ListComprehension.py: Demo code for List Comprehension"""

__author__ = "Sumit Kala"
'''List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc.
   A list comprehension consists of brackets containing the expression, which is executed for each element along with the 
   for loop to iterate over each element. 
   
   Syntax:
   newList = [ expression(element) for element in oldList if condition ]
   '''


def ListCreator():

    mylist = range(10)
    yield mylist
    mylist2 = [x ** 2 for x in range(5)]  # list of squares from 0-4
    yield mylist2

    mylist3 = [(x, x * 2) for x in range(10)]  # list of tuples
    yield mylist3


def main():
    x = ListCreator()
    # print 100 to 70

    for i in x.__next__():
        print(f'{i}', end=" ")  # print in same line
    print(f'')
    for i in x.__next__():
        print(f'{i}', end=" ")  # print in same line
    print(f'')
    for i in x.__next__():
        print(f'{i}', end=" ")  # print in same line


if __name__ == '__main__':
    main()
