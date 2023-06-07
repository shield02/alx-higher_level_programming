#!/usr/bin/python3
def magic_string(w=[0]):
    w[0] += 1
    return str("BestSchool, " * (w[0] - 1)) + "BestSchool"
