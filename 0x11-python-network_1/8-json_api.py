#!/usr/bin/python3
"""
This module contains a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ''
    parameter = {"q": letter}
    res = requests.post("http://0.0.0.0:5000/search_user", data=parameter)
    try:
        json = res.json()
        if len(json) > 0:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
