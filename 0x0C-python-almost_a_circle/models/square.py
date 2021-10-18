#!/usr/bin/python3
"""Define a square object.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a square object.

    Attributes:
        size: size square side
        x: int indicates space in axis x
        y: int indicates space in axis y
        id: int unique identification
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Inits Square class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Make a string representation of object instance.

        Returns:
            String representation of object instance.
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter size.
        """
        return self.width

    @size.setter
    def size(self, size):
        """Setter size.

        Args:
            size: square side size
        Raises:
            TypeError: width must be an integer
            ValueError: width mush > 0
        """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        super().update(width=size, height=size)

    def update(self, *args, **kwargs):
        """Update instance object.

        Args:
            *args: non-keyworked tuple
            **kwargs: keyworked dictionary
        """
        if args or len(args) > 0:
            for i in range(len(args)):
                # id
                if i == 2:
                    self.id = args[i]
                # size
                if i == 3:
                    print(args[i])
                    self.width = args[i]
                    self.height = args[i]
                # x
                if i == 1:
                    self.x = args[i]
                # y
                if i == 0:
                    self.y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs.get(key)
                if key == "size" or key == "width":
                    self.width = kwargs.get(key)
                    self.height = kwargs.get(key)
                if key == "x":
                    self.x = kwargs.get(key)
                if key == "y":
                    self.y = kwargs.get(key)

    def to_dictionary(self):
        """Make a dictionary representation object.

        Returns:
            Dictionary representation object.
        """
        d = {
            'id': self.__dict__['id'],
            'x': self.__dict__['_Rectangle__x'],
            'size': self.__dict__['_Rectangle__width'],
            'y': self.__dict__['_Rectangle__y'],
        }
        return d
