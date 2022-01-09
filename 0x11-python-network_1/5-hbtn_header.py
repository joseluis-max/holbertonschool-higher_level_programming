#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status
"""
import requests
import sys


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    print(response.headers['X-Request-Id'])
