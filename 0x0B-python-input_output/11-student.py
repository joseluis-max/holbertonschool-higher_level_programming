#!/usr/bin/python3
""" Class Student """


class Student:
    """ Define Student
        Attributes:
            first_name: string
            last_name: string
            age: int
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return self.__dict__
        n_d = {}
        for attr in attrs:
            if attr in self.__dict__ and type(attr) is str:
                n_d[attr] = self.__dict__.get(attr)
        return n_d

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        att = self.__dict__
        for key in json:
            if key in self.__dict__:
                att[key] = json.get(key)
