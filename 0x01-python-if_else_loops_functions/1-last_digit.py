#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigit = ((number * -1) % 10) * -1
else:
    lastDigit = number % 10
if lastDigit > 5:
    print("Last digit of {:d} is {:d} and is greather than 5".format(number, lastDigit))
elif lastDigit < 6:
    print("Last digit of {:d} is {:d} and is less than 6    ".format(number, lastDigit))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, lastDigit))

