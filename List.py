#!/usr/bin/env python

"""List.py: Demo code for python Lists"""

__author__ = "Sumit Kala"
'''The list is a most versatile datatype available in Python which can be written as a 
    list of comma-separated values (items) between square brackets. 
    Important thing about a list is that items in a list need not be of the same type.'''


def myList():
    list = ['Sumit', '48', 'M', '560035', 'BLR']
    return list


def AddToList(mylist, item):
    #if item != 'z':
    mylist.append(item)

def DelFromList(mylist):
    mylist.pop()

def main():
    x = myList()
    for i in x:
        print(f'{i}')
    x[1] = 40  # modify the age
    x.append('India')  # add an element at last.
    for i, value in enumerate(x):  # print index and value of list
        print(f'{i},{" "}{value}')
    x.pop(3)  # pop the third element
    for i, value in enumerate(x):  # print index and value of list
        print(f'{i},{" "}{value}')
    ll = []
    AddToList(ll, 'a')


if __name__ == '__main__':
    main()
