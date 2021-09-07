#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lD = ((n * -1) % 10) * -1
else:
    lD = number % 10
if lD > 5:
    print("Last digit of {} is {} and is greather than 5".format(number, lD))
elif lD < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lD))
else:
    print("Last digit of {} is {} and is 0".format(n, lD))
