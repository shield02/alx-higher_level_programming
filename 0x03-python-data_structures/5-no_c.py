#!/usr/bin/python3
def no_c(my_string):
    outstring = ''

    for char in my_string:
        if char in ['c', 'C']:
            continue
        outstring += char

    return outstring
