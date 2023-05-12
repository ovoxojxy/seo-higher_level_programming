#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ''
    for char in str:
        uppercase_str += chr(ord(char) - 32) if 'a' <= char <= 'z' else char
    print('{}\n'.format(uppercase_str))
