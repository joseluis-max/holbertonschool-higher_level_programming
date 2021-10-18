#!/usr/bin/python3
from models.base import Base
"""Define a Rectangle Object.
"""


class Rectangle(Base):
    """Class Rectangle definition.

    Arguments:
        width: int indicates the width
        height: int indicates the height
        x: int indicates space in axis x
        y: int indicates space in axis y
        id: int indicates unique identification

    Raises:
        TypeError: with, height, y or x aren't integers
        ValueError: width, height, y or x are less(or equal) that 0
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("x must must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    def __str__(self):
        """String Representation Object.

            Returns:
                String representation object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        """Getter width.
        """
        return self.__width

    @property
    def height(self):
        """Getter height.
        """
        return self.__height

    @property
    def x(self):
        """Getter x.
           """
        return self.__x

    @property
    def y(self):
        """Getter y.
        """
        return self.__y

    @width.setter
    def width(self, width):
        """Setter width.

            Args:
                width: int indicates width of the rectangle
            Raises:
                TypeError: width not is a integer
                ValueError: width is less than 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Setter height.

            Args:
                height: int indicates height of the rectangle
            Raises:
                TypeError: height not is a integer
                ValueError: height is less than 0
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Setter x.

        Args:
            x: int indicates space in axis x
        Raises:
            TypeError:x not is a integer
            ValueError: x is less than or equal to 0
        """
        if type(x) is not int:
            raise TypeError("x must must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Setter y.

        Args:
            y: int indicates space in axis y
        Raises:
            TypeError: y not is a integer
            ValueError: y is less than or equal to 0
        """
        if type(y) is not int:
            raise TypeError("x must must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate area rectangle.

        Returns:
            Area of rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """Print in screen the rectangle with #
        """
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            print("#" * self.__width, end="")
            print()

    def update(self, *args, **kwargs):
        """Update attributes of instance object.
        """
        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs.get(key)
                if key == "width":
                    self.__width = kwargs.get(key)
                if key == "height":
                    self.__height = kwargs.get(key)
                if key == "x":
                    self.__x = kwargs.get(key)
                if key == "y":
                    self.__y = kwargs.get(key)

    def to_dictionary(self):
        """Make a dictionary object representation.

        Returns:
            Dictionary object representation.
        """
        d = {
            'x': self.__dict__['_Rectangle__x'],
            'y': self.__dict__['_Rectangle__y'],
            'id': self.__dict__['id'],
            'height': self.__dict__['_Rectangle__height'],
            'width': self.__dict__['_Rectangle__width'],
        }
        return d
