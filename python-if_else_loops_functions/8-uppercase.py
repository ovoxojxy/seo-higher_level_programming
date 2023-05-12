#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        str_int = ord(str[i])
        if chr(str_int).islower() == True:
            new_string = chr(str_int - 32)
            print('{0}'.format(new_string), end = '')
        else:
            print(chr(str_int), end = '')
    print(' ')
