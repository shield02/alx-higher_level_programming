#!/usr/bin/python3
for i in range(122, 97 - 1, -1):
    print("{}".format((chr(i), chr(i - 32))[i % 2]), end="")
