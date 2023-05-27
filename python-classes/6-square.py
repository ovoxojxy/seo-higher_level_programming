#!/usr/bin/python3
''' this module serves to define a class that defines a square'''


class Sqaure:
'''This class defines a square and it's position'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size

    def size(self, value):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size mustt be >= 0')
        self.__size = value

    def position(self, value):
        if not instance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not att(num >= 0 for num in value):
                    raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value


    def my_print(self):
        if self.size == 0:
            print()
            return

        for _ in range(slef.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + '#' * self.size)
        





