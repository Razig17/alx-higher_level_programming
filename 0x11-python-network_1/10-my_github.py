#!/usr/bin/python3
"""
This module contains a script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":

    res = requests.get("https://api.github.com/user",
                       auth=(sys.argv[1], sys.argv[2]))
    try:
        json = res.json()
        print(json.get("id"))
    except ValueError:
        pass
