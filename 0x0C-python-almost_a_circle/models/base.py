#!/usr/bin/python3
"""Define a Base Constructor.
"""
import json
import csv
import turtle
import random


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
        """Save dictionaries objects representation
        in a file like json strings.
        """
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
                A list with instances of cls with
                values update to values dictionaries
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save dictionaries objects representation in a csv file"""
        with open(cls.__name__ + ".csv", 'w', newline='') as csvfile:
            spam_writer = csv.writer(csvfile, delimiter=',')
            for dic in list_objs:
                values = []
                values.append(dic.__dict__.get("id"))
                values.append(dic.__dict__.get("_Rectangle__width"))
                if dic.__dict__.get("_Rectangle__width") \
                        != dic.__dict__.get("_Rectangle__height"):
                    values.append(dic.__dict__.get("_Rectangle__height"))
                values.append(dic.__dict__.get("_Rectangle__x"))
                values.append(dic.__dict__.get("_Rectangle__y"))
                spam_writer.writerow(values)

    @classmethod
    def load_from_file_csv(cls):
        """Load dictionaries from csv file and create
        new instances of cls with values directories

            Returns:
                A list with new instances of cls with values from dictionaries
        """
        dict_list = []
        instances = []
        with open(cls.__name__ + ".csv") as file:
            for line in file:
                line = line.strip().split(',')
                d = {}
                if cls.__name__ == "Rectangle":
                    f = ["id", "width", "height", "x", "y"]
                    for item, value in zip(f, line):
                        d[item] = int(value)
                    dict_list.append(d)
                if cls.__name__ == "Square":
                    f = ["id", "size", "x", "y"]
                    for item, value in zip(f, line):
                        d[item] = int(value)
                    dict_list.append(d)
            for dic in dict_list:
                ins = cls.create(**dic)
                instances.append(ins)
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw with Turtle module."""
        turtle.title("Squares and Rectangles")
        turtle.up()
        for rec in list_rectangles:
            turtle.setpos(random.randrange(-200, 200),
                          random.randrange(-200, 200))
            turtle.down()
            turtle.fillcolor("yellow")
            turtle.begin_fill()
            turtle.forward(rec.width)
            turtle.left(90)
            turtle.forward(rec.height)
            turtle.left(90)
            turtle.forward(rec.width)
            turtle.left(90)
            turtle.forward(rec.height)
            turtle.end_fill()
            turtle.up()
        for squ in list_squares:
            turtle.setpos(random.randrange(-200, 200),
                          random.randrange(-200, 200))
            turtle.fillcolor("green")
            turtle.begin_fill()
            turtle.down()
            turtle.forward(squ.width)
            turtle.left(90)
            turtle.forward(squ.width)
            turtle.left(90)
            turtle.forward(squ.width)
            turtle.left(90)
            turtle.forward(squ.width)
            turtle.left(90)
            turtle.end_fill()
            turtle.up()
        turtle.done()
