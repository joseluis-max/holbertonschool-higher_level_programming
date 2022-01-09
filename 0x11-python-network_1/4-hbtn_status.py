#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('    - type: ', end='')
        print(type(html))
        print('    - content: ', end='')
        print(html.decode('utf-8'))
