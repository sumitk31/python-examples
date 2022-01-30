#!/usr/bin/env python

"""Sets.py: Demo code for Sets"""
__author__ = "Sumit Kala"

'''In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements. 
   The order of elements in a set is undefined though it may consist of various elements.
   The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking 
   whether a specific element is contained in the set.'''


def mySet():
    myset = set("abc122ahjcbmks5643274")
    return myset


def main():
    x = mySet()
    print(f'{x}')  # prints unique elements in unordered fashion
    print(f'{sorted(x)}')  # prints unique elements in the set in order


if __name__ == '__main__':
    main()
