#!/usr/bin/python3
""" Inherance List """


class MyList(list):
    """ Print list in ascending order"""

    def print_sorted(self):
        """print list sorted"""
        print(sorted(self))
