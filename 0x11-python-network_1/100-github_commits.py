#!/usr/bin/python3
"""
This module contains a script that uses the GitHub API to
get the last 10 commits from a repository
"""
import sys
import requests

if __name__ == "__main__":

    res = requests.get(f"https://api.github.com/repos/{sys.argv[2]}/"
                       f"{sys.argv[1]}/commits")
    try:
        commits = res.json()
        for i in range(10):
            commit = commits[i]
            sha = commit.get('sha')
            user = commit.get('commit').get('author').get('name')
            print(f"{sha}: {user}")

    except (ValueError, IndexError):
        pass
