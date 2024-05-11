#!/usr/bin/python3
"""
This module contains a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.get(sys.argv[1])
    status = res.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(res.text)
