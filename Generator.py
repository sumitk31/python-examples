#!/usr/bin/env python

"""Generator.py: Demo code for Generator functions"""

__author__ = "Sumit Kala"
'''Generator-Function : A generator-function is defined like a normal function, but whenever it needs to generate a value,
 it does so with the yield keyword rather than return.If the body of a def contains yield, the function automatically 
 becomes a generator function.'''

'''Generator-Object : Generator functions return a generator object. 
Generator objects are used either by calling the next method on the generator object or using the generator object in a “for in” loop'''
def myGenerator():
    i = 100
    while i>0:
        if i%10 == 0:
            yield i
        i-=1

def main():
    x = myGenerator()
    #print 100 to 70
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print("printing using for now")
    for i in x:
        print(i)
if __name__ == '__main__':
        main()