#!/usr/bin/python3
"""
This module contains a script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
