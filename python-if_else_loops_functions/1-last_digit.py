#!/usr/bin/python3
import random
number = random.ranint(-10000, 10000)
if number > 0:
    last_digit = abs(number) % -10
else:
    last_digit = abs(number) % 10

digit = f"Last digit of {number} is {last_digit}"

if last_digit > 5:
   print("digit += " and is greater than 5")
elif last_digit == 0:
   print("digit += " and is 0")
else:
   print("digit += " and is less than 6 and is not 0")
