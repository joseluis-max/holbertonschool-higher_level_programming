#!/usr/bin/python3
""" Crate a class that define a square with methods
    and setter, getter, print, my_print advanced """


class Square:
    """
    Square define a square

    Attributes
    ----------
    size: int
        size square side
    position: tuple
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters
        ----------
        size: int
            size square side (default 0)
        position: tuple
            two positive integers
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

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """
        To get the value of position

        Returns: value of position

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Changes value of size attribute
        Args
        ____
            value: tuple
                tuple of two positive integers
        Raise
        _____
            TypeError: if not is a tuple
            ValueError: if is less than 0
        """

        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[1] < 0 or value[0] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """ Print a square of # with the same long of size """

        if self.__size != 0:
            if self.__position[1] is not 0:
                print('\n', end="")
            for n in range(0, self.__size):
                for s in range(0, self.position[0]):
                    print(end=" ")
                for m in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()
