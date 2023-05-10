#!/usr/bin/python3

for i in range(97, 123):                                                                                     
    letter = chr(i)
    if (letter != chr(101) and letter != chr(113)):
        print(f'{letter}'.format(letter), end='')  
