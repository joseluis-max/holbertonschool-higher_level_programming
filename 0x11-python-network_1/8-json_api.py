#!/usr/bin/python3
""" script that takes in a letter and sends a
    POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':  
    try:
        arg = sys.argv[1]
    except Exception:
        arg = ""
    q = {"q": arg}
    req = requests.post("http://0.0.0.0:5000/search_user", data=q)
    try:
        result = req.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(result['id'], result['name']))
    except Exception:
        print("No result")