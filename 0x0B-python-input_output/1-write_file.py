#!/usr/bin/python3
""" Written a file """


def write_file(filename="", text=""):
    """ Write a file with write method """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
