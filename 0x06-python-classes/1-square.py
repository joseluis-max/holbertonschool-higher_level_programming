#!/usr/bin/python3
"""Create a class that define square"""


class Square:
    """
    Square define a square

    Attributes
    ----------
    size: int
        size square side
    """

    def __init__(self, size):
        """
        Parameters
        ----------
        size: int
            size square side
        """
        self.__size = size
