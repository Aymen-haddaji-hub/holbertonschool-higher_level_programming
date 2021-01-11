#!/usr/bin/python3
"""
send a get requests and display the response
"""


import requests

if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
