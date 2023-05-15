#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = - 1
    z = None
    if my_list != z:
        for i in range(len(my_list)):
            print('{:d}'.format(my_list[x]))
            x -= 1
