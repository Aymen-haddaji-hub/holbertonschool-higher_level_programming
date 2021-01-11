#!/usr/bin/python3
"""Python script that takes in a URL and an email,\
     sends a POST request to the passed URL with the email as a parameter,\
     and displays the body of the response (decoded in utf-8)
"""


import requests
from sys import argv

if __name__ == '__main__':
    try:
        url = argv[1]
        mail_adress = {"email": argv[2]}
        data = requests.post(url, data=mail_adress)
        print(data.text)
    except Exception:
        if not argv[1] or argv[2]:
            pass
        