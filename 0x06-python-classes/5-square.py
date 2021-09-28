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

    @property
    def size(self):
        """
        To get the value of size

        Returns: value of size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Changes value of size attribute
        Args
        ____
            value: int
                new value of size
        Raise
        _____
            TypeError: if not is a number
            ValueError: if is less than 0
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Print a square of # with the same long of size
        """

        if self.__size != 0:
            for n in range(0, self.__size):
                for m in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()
