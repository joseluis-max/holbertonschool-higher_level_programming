#!/usr/bin/python3
import json
""" json representation object """


def to_json_string(my_obj):
    """
    encoding a object
    Return:
        my_obj representation object
    """
    return json.dumps(my_obj)
