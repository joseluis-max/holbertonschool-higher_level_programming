#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lD = ((number * -1) % 10) * -1
else:
    lD = number % 10
print("Last digit of ", end="")
if lD > 5:
    print("{:d} is {:d} and is greather than 5".format(number, lD))
elif lD < 6 and lD != 0:
    print("{:d} is {:d} and is less than 6 and not 0".format(number, lD))
else:
    print("{:d} is {:d} and is 0".format(number, lD))
