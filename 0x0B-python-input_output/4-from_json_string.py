#!/usr/bin/python3
import json
""" Json String to Object Python"""


def from_json_string(my_str):
    """ decoding a json string """
    return json.loads(my_str)
