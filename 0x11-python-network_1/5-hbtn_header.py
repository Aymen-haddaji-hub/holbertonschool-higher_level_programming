#!/usr/bin/python3
"""Python script that takes in a URL\
    sends a request to the URL and displays the value of \
    the X-Request-Id variable found in the header of the response.
"""


from sys import argv
from requests import get

if __name__ == "__main__":
    response = get(argv[1])
    print(response.headers.get('X-Request-Id'))
