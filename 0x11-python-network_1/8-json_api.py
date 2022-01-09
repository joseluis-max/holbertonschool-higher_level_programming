#!/usr/bin/python3
""" script that takes in a letter and sends a
    POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv[1]) == 2:
        q = sys.argv[1]
    else:
        q = ""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        d = res.json()
        id = d.get('id')
        name = d.get('name')
        if len(d) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(d.get('id'), d.get('name')))
    except Exception:
        print("Not a valid JSON")
