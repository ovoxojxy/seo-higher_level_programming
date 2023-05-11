#!/usr/bin/python3
for i in range (0, 100):
    num = str(i).zfill(2)
    print("{0}".format(num), end = ', ' if i < 99 else "\n")
