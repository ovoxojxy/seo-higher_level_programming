#!/usr/bin/python3                                                       
''' This is to write a class that makes a square by taking in an argument for size'''            

                                                                                                                                                  class Square:
                                                                                                                                                      '''This class defines a square'''
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
