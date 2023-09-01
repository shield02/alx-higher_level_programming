#!/usr/bin/python3
"""take a URL, send a request to the URL and displays the value of the
   X-Request-Id variable found in the header response"""
from sys import argv
import urllib


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as r:
        print(r.headers.get('X-Request-Id'))
