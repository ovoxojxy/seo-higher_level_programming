#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    y = -1 *(abs(number)%10)
elif(number >= 0):
    y = number%10
number = x
if(y > 5):
    print(f"Last digit of {x} is {y} and is greater than 5")
elif(y < 6 and y != 0):                                         
    print(f"Last digit of {x} is {y} and is less than 6 and not 0")
elif(y ==0):
    print(f"Last digit of {x} is {y} and is 0")
