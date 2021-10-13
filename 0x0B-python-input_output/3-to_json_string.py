#!/usr/bin/python3
""" json representation object """
import json


def to_json_string(my_obj):
    """
    encoding a object
    Return:
        my_obj representation object
    """
    return json.dumps(my_obj)
