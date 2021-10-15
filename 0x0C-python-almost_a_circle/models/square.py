#!/usr/bin/python3

from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        super().update(width=size, height=size)

    def update(self, *args, **kwargs):
        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs.get(key)
                if key == "size":
                    self.width = kwargs.get(key)
                    self.height = kwargs.get(key)
                if key == "x":
                    self.x = kwargs.get(key)
                if key == "y":
                    self.y = kwargs.get(key)

    def to_dictionary(self):
        d = {
            'id': self.__dict__['id'],
            'x': self.__dict__['_Rectangle__x'],
            'size': self.__dict__['_Rectangle__width'],
            'y': self.__dict__['_Rectangle__y'],
        }
        return d
