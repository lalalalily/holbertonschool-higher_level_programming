#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0: 
    k = "is positive"
elif number == 0: k = "is zero"
else: k = "is negative"
print(f"{number} k")
