#!/usr/bin/python3
""" Class Rectangle define a Rectangle """


class Rectangle:
    """ Define a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Constructor
        Args:
            width: width of rectangle
            height: height of rectangle
        Exp:
            TypeError: w and h must be integer
            ValueError: w and h must be great than o equal to zero
        """

        if type(width) is int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if type(height) is int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def __str__(self):
        """
        Print in display the rectangle with #
        Returns: str with format
        """

        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        for w in range(self.__height):
            for h in range(self.__width):
                s += "#"
            s += "\n"
        return s

    @property
    def width(self):
        """
        Getter of width
        Return: rectangle width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter of width
        Args:
            value: new rectangle width
        Exp:
            TypeError: value no is integer
            ValueError: value is < 0
        """

        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        Getter of height
        Returns: height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter of height

        Args:
            value: new rectangle width
        Exp:
            TypeError: value no is integer
            ValueError: value is < 0

        Returns: void

        """

        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """
        Calculate area rectangle
        Returns: area

        """

        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate perimeter rectangle
        Returns: perimeter
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)