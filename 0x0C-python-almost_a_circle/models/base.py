#!/usr/bin/python3
"""Define a Base Constructor.
"""
import json


class Base:
    """Define a Base Constructor.

    Base Constructor define a id Attribute for every
    instance of Base created.

    Attributes:
        id: identification for every instance of Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Inits Base Class with id None by default or id receive."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a dictionary in json string."""
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save dictionaries objects representation in a file like json strings."""
        with open(cls.__name__ + ".json", "w") as file:
            if len(list_objs) == 0:
                file.write("[]")
            else:
                s = []
                for item in list_objs:
                    d = {
                        'y': item.__dict__['_Rectangle__y'],
                        'x': item.__dict__['_Rectangle__x'],
                        'id': item.__dict__['id'],
                        'width': item.__dict__['_Rectangle__width'],
                        'height': item.__dict__['_Rectangle__height'],
                    }
                    s.append(d)
                file.write(Base.to_json_string(s))

    @staticmethod
    def from_json_string(json_string):
        """Convert json string representation in a dictionary."""
        if json_string is None:
            return "[]"
        if len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance of a cls class with dictionary values."""
        rec = cls(1, 1)
        rec.update(**dictionary)
        return rec

    @classmethod
    def load_from_file(cls):
        """Load dictionaries from json file and
            create new instances of cls with values directories

            Returns:
                A list with instances of cls with values update
                to values dictionaries
        """
        instances = []
        try:
            with open(cls.__name__ + ".json", "r") as file:
                _list = cls.from_json_string(file.read())
        except OSError:
            return instances
        for dic in _list:
            ins = cls.create(**dic)
            instances.append(ins)
        return instances
