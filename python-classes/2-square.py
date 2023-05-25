#!/usr/bin/python3
'''This module is here to create a class that defines a square with a private instance attribute and instantiation'''


class Square:
    '''This class defines a sqaure and verifies the type of the size variable and it being greater than 0'''

    def __init__(size, size=0):
        ''' This constructor initializes the class'''
        self._Square__size = size

