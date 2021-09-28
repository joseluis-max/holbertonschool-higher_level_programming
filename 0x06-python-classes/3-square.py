#!/usr/bin/python3
class Square:
    """
    Square define a square

    Attributes
    ----------
    size: int
        size square side
    """

    def __init__(self, size=0):
        """
        Parameters
        ----------
        size: int
            size square side (default 0)
        Raises
        ------
            TypeError: if not is a number
            ValueError: if is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area square

        Returns: Square area
        """

        return self.__size * self.__size
