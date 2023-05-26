#!/usr/bin/python3
''' This module defines sqaures and blah blah blah'''
class Square:
    ''' Documentation test chekc for class'''
    def __init__(self, size=0):
        self.size = size
    def area(self):
        return self.size ** 2

try:
    my_square = Square(89)
    print(my_square.size)
    my_square.size = '89'
    print(my_sqaure.size)
except Exception as e:
    print('size must be an integer')

