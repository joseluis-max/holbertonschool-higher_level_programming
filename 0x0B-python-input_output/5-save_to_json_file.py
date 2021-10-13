#!/usr/bin/python3
""" Write object representation json string in a file """

import json


def save_to_json_file(my_obj, filename):
    """ Write object representation json string in a file """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
