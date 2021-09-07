#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        number = ord(str[i])
        if number >= 97 and number <= 122:
            number -= 32
        print("{:c}".format(number), end="")
    print()
