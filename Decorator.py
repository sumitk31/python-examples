#!/usr/bin/env python

"""Decorator.py: Demo code for Decorator functions"""
__author__ = "Sumit Kala"

'''Python developers can extend and modify the behavior of a callable functions, methods or classes without permanently 
modifying the callable itself by using decorators. In short we can say they are callable objects which are used to modify functions or classes.

Function decorators are functions which accepts function references as arguments and adds a wrapper around them and 
returns the function with the wrapper as a new function.'''


# Python program to explain property()
# function using decorator

class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the values
    @property
    def value(self):
        print('Getting value')
        return self._value

    # setting the values
    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value


# passing the value
x = Alphabet('Peter')
print(x.value)

x.value = 'Diesel'

del x.value
