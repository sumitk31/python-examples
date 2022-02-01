#!/usr/bin/env python

"""ClassEx.py: Demo code for Class"""
__author__ = "Sumit Kala"

'''Class − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class.
   The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
Class variable − A variable that is shared by all instances of a class. Class variables are defined within a class but 
                 outside any of the class's methods. Class variables are not used as frequently as instance variables are.
Data member − A class variable or instance variable that holds data associated with a class and its objects.
Function overloading − The assignment of more than one behavior to a particular function. The operation performed varies
                       by the types of objects or arguments involved.
Instance variable − A variable that is defined inside a method and belongs only to the current instance of a class.
Inheritance − The transfer of the characteristics of a class to other classes that are derived from it.
Instance − An individual object of a certain class. An object obj that belongs to a class Circle, for example, 
           is an instance of the class Circle.
Instantiation − The creation of an instance of a class.
Method − A special kind of function that is defined in a class definition.
Object − A unique instance of a data structure that's defined by its class. An object comprises both data members 
         (class variables and instance variables) and methods.
Operator overloading − The assignment of more than one function to a particular operator.
'''


class Student:
    def __init__(self, name="", age="", roll=""):  # constructor

        self._name = name
        self._age = age
        self._roll = roll

    def __getitem__(self, key):  # getter based on indexing and getattribte
        return self.__getattribute__(key)

    def __setitem__(self, key, value):  # setter based on indexing and setattr
        return self.__setattr__(key, value)

    def getName(self):  # getter for Name
        return self._name

    def setName(self, value):  # setter for Name
        self._name = value

    def __str__(self):  # string representtion of the class
        return (self._name + " " + str(self._age) + " " + str(self._roll))


def main():
    student1 = Student('sumit', 38, 1)
    print(student1["_name"])  # print using __getitem__
    print(student1["_age"])  # print using __getitem__
    print(f'{student1._name}{" "}{student1._age}{" "}{student1._roll}')
    student1["_roll"] = 5
    student1.setName("Victor")
    print(f'{student1._name}{" "}{student1._age}{" "}{student1._roll}')
    print(f'{student1.getName()}{" "}{student1._age}{" "}{student1._roll}')
    student2 = Student()
    student2["_name"] = 'Megha'
    student2["_age"] = 35
    student2["_roll"] = 6
    print(f'{student2.__str__()}')  # get the string representaion of the class


if __name__ == '__main__':
    main()
