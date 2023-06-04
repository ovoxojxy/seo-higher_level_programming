#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    new_list = []
    if len(list_a) == len(list_b):
        if len(tuple_a) == 0 and len(tuple_b) == 0:
            tup = (0, 0)
        else:
            for i in range(len(list_a)):
                tup = (tuple_a[0] +tuple_b[0], tuple_a[1] + tuple_b[1])
    elif (len(list_a) > len(list_b)):
        for i in range(len(list_a) - len(list_b)):
            list_b.append(0)
        for i in range(len(list_a)):
            new_list.append(list_a[i] + list_b[i])
        tup = tuple(new_list)
    elif (len(list_a) < len(list_b)):
        for i in range(len(list_b) - len(list_a)):
            list_a.append(0)
        for i in range(len(list_a)):
            new_list.append(list_a[i] + list_b[i])
        tup = tuple(new_list)
    elif len(list_a) and len(list_b) == 0:
        new_list.append(0)
        new_list.append(0)
        tup = tuple(new_list)
    return tup
