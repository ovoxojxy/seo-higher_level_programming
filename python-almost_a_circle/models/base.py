#!/usr/bin/python3
''' This modules purpose is to creat the first class called base'''


class Base:
    ''' The purpose of this class is to have the public instance variable ID'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id != none:
            return id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
