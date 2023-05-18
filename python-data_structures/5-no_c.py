#!/usr/bin/python3
def no_c(my_string):
    word = my_string
    new_word = (my_string.translate({ord(i): None for i in 'cC'}))
