#!/usr/bin/env python

"""Dictionary.py: Demo code for Dictionary"""
__author__ = "Sumit Kala"

'''Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is 
   enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.
   Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type,
   but the keys must be of an immutable data type such as strings, numbers, or tuples.'''

def mydict():
    mydictionary = {'Name':'Sumit','Age':38,'Gender':'Male','Country':'India'}
    return mydictionary

def main():
    x = mydict()
    for k,v in x.items():
        print(f'{k}{" "}{v}')
    keys = x.keys()
    for k in keys:
        print(f'{k}')
    values = x.values()
    for v in values:
        print(f'{v}')

if __name__ == '__main__':  # forces the interpreter to read the complete file before execution
        main()