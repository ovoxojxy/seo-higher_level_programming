#!/usr/bin/python3
''' This module defines sqaures and blah blah blah'''


class Square:
    ''' Documentation test chekc for class'''
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size ** 2
    
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__ = value
