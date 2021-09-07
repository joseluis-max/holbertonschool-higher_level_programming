#!/usr/bin/python3
for i in range(10):
    for o in range(10):
        if i != o:
            if int(str(i) + str(o)) < int(str(o) + str(i)):
                if i != 8:
                    print("{:d}{:d}".format(i, o), end=", ")
                else:
                    print("{:d}{:d}".format(i, o))
