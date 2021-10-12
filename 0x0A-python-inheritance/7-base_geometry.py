#!/usr/bin/python3
""" BaseGeometry """


class BaseGeometry:
    """ BaseClass """

    def area(self):
        """ Area definition """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate Value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
