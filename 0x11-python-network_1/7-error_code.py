#!/usr/bin/python3
"""send a request to a given URL and displays the response body
  - andle HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
