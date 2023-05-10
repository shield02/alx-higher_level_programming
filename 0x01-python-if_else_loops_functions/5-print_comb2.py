#!/usr/bin/python3
for d in range(0, 100):
    print("{:02d}".format(d), end="")
    print(("\n", ", ")[d != 99], end="")
