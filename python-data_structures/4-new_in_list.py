#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx >= 0 and idx < len(my_list):
        for i in range(len(my_list)):
            if i != idx:
                new_list.append(my_list[i])
            elif i == idx:
                new_list.append(element)
                return new_list
            else:
                return my_list
