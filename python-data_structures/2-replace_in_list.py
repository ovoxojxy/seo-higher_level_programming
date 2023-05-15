#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        list = my_list
        b = list
        list[idx] = element
        return b
    else:
        return my_list
