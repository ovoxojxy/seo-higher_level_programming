#!/usr/bin/python3
''' This module is to define a class that prints a square'''


class Square:
    ''' This class prints a square '''
    def __init__(self, size=0):
        self._Square__size = size    
            
    def area(self):
        return self._Square__size ** 2
                
    def my_print(self):
        if size > 0:
            for i in range(self._Square__size):
                for x in range(self._Square__size):
                    print('#', end='')
                print(sep='\n')
        elif size = 0:
            return ' '
