#!/usr/bin/python3
"""
This module contains a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    parameter = {"email": email}
    res = requests.post(url, data=parameter)
    print(res.text)
