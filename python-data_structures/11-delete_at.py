#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        x = my_list[idx]
        new_list = my_list
        new_list.remove(x)
        return new_list
    else:
        return my_list
