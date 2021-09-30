#!/usr/bin/python3
""" Class Rectangle define a Rectangle """


class Rectangle:
    """
    Define a Rectangle

    Attributes:
        number of instances: int
            counter of instances
        print symbol: any type
            symbol for print
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

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
                s += str(self.print_symbol)
            s += "\n"
        return s

    def __repr__(self):
        """
        Make a string in representation on the object
        Returns: string object representation
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when instance is delete and less counter instances"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Calculate the area more biggest
        Args:
            rect_1: Rectangle object
            rect_2: Rectangle object
        Exp:
            TypeError: if rect1 or rect2 must be Rectangle instance

        Returns: Rectangle with are more biggest

        """

        if type(rect_1) is Rectangle:
            if type(rect_2) is Rectangle:
                if rect_1.area() > rect_2.area():
                    return rect_1
                elif rect_1.area() < rect_2.area():
                    return rect_2
                else:
                    return rect_1
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
