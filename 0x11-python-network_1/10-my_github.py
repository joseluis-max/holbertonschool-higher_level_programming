#!/usr/bin/python3
""" GitHub Api"""
import requests
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    token = argv[2]
    url = 'https://api.github.com/user'

    r = requests.get(url, auth=(user, token))
    print(r.json().get("id"))
