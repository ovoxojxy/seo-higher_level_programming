#!/usr/bin/python3
import random                                                                            
number = random.randint(-10000, 10000)
num_str = str(number)
numcon = int(num_str[-1])
if (numcon > 5):
        print(f"Last digit of {number} is {numcon} and is greater than 5")
elif (numcon < 6 and numcon != 0):
        print(f"Last digit of {number} is {numcon} and is less than 6 and not 0")
elif (numcon == 0):
        print(f"Last digit of {number} is {numcon} and is 0")
