#!/usr/bin/python3
""" Json String to Object Python"""
import json


def from_json_string(my_str):
    """ decoding a json string """
    return json.loads(my_str)
