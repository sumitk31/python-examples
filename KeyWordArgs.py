#!/usr/bin/env python

"""KeyWordArgs.py: Demo code for kwargs in function"""

__author__      = "Sumit Kala"

def main():
    mydict = dict(Name ='Sumit',Age = 38,Loc = 'IN')
    myFunc(**mydict)

def myFunc(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print(kwargs[k])

if __name__ == '__main__':  # forces the interpreter to read the complete file before execution
        main()