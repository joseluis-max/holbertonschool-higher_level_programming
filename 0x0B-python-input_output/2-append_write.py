#!/usr/bin/python3
""" Append a file """


def append_write(filename="", text=""):
    """ Append a file with write method """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
