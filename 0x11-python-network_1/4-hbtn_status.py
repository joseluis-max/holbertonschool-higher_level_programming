#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: ', end='')
    print(type(response.content.decode('utf-8')))
    print('\t- content: ', end='')
    print(response.text)
