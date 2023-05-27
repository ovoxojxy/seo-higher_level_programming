#!/usr/bin/python3
''' This module's purpose is to define a class that defines a square and validates it's size with TypeError and ValueError functions'''


class Square:
    '''This class defines a sqaure and verifies the type of the size variable and it being greater than 0'''
    def __init__(self, size=0):
        ''' This constructor initializes the class'''
        if size => 0 and type(size) is int:
            self._Square__size = size
        elif size < 0:
           try:
               print(x)
            except ValueError:
                print('size must be >= 0')
        elif type(size) != int:
            try:
                print(x)
            except TypeError:
                print('size must be an integer')


