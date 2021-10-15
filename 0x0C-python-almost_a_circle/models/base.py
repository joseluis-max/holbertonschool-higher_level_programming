#!/usr/bin/python3
""" Define a Base Constructor """
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", "w") as file:
            if len(list_objs) == 0:
                file.write("[]")
            else:
                s = []
                for item in list_objs:
                    s.append(item.__dict__)
                file.write(Base.to_json_string(s))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        if len(json_string) == 0:
            return "[]"
        return json.loads(json_string)
