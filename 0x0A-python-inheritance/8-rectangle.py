#!/usr/bin/python3
""" BaseGeometry """


class BaseGeometry:
    """ BaseClass """

    def area(self):
        """ Area definition """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate Value """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseException):
    """ Define a Rectangle """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
