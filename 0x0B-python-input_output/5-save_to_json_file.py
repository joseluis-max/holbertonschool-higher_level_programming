#!/usr/bin/python3
import json
""" Write object representation json string in a file """


def save_to_json_file(my_obj, filename):
    """ Write object representation json string in a file """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
