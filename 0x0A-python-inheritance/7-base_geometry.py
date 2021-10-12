#!/usr/bin/python3
""" BaseGeometry """


class BaseGeometry:
    """ BaseClass """

    def area(self):
        """ Area definition """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate Value """

        if type(name) is not str:
            raise TypeError("{} must be a string".format(name))
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
