#!/usr/bin/python3
def max_integer(my_list=[]):
    x = my_list[0]
    if len(my_list) > 0:
        for i in my_list:
            if i > x:
                x = i
    else:
        x = None
    return x

