#!/usr/bin/python3
import random
x = random.randint(-10000, 10000)
if (x < 0):
    y = -1 *(abs(x)%10)
elif(x >= 0):
    y = x%10
if(y > 5):
    print(f"Last digit of {x} is {y} and is greater than 5")
elif(y < 6 and numcon != 0):                                         
    print(f"Last digit of {x} is {y} and is less than 6 and not 0")
elif(y ==0):
    print(f"Last digit of {x} is {y} and is 0")
