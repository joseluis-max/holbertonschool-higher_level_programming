#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
if n < 0:
    lD = ((n * -1) % 10) * -1
else:
    lD = n % 10
if lD > 5:
    print("Last digit of {} is {} and is greather than 5".format(n, lD))
elif lD < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, lD))
else:
    print("Last digit of {} is {} and is 0".format(n, lD))
