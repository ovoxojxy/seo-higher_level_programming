#!/usr/bin/python3                                                       
''' This module creates a class Square that defines a square by taking'''       


class Square:
    def __init__(self, size=0):
    ''' This method serves as a constructor '''
        self._Square__size = size

    def area(self):
        return self._Square__size ** 2 
