#!/usr/bin/python3
''' This module is for accessing and updating attributes'''


class Square:
    ''' This class ishere to define a sqaure'''
    def __init__(self, size=0):
        self.__Square_size = size

    def size(self, value):
        self.value = value

    def area(self, size):
        return self.size ** 2


