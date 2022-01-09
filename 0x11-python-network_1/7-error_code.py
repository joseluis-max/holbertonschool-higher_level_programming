#!/usr/bin/python3
""" script that takes in a URL, sends a request to the
    URL and displays the body of the response.
"""
import requests
import sys


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    try:
        response.raise_for_status()
        print(response.content.decode('utf-8'))
    except Exception:
        print(response.status_code)
