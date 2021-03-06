#!/usr/bin/python3
""" Class rectangle that inherits from BaseGeometry class """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Class rectangle that inherits from BaseGeometry class """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    """ Return rectangle area """

    def area(self):
        return self.__width * self.__height
    """ Return rectangle size """

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
