#!/usr/bin/python3
"""
This module contains a Python script that takes in a URL,
sends a request to the URL and displays the body of the response
(decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
