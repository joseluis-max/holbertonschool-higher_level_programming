#!/usr/bin/python3
""" Reading a file and print it in screen """


def read_file(filename=""):
    """ Read and print a file on screen """

    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file.readlines():
            print(line, end="")
