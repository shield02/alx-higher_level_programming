#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    output = ""
    for letter in str:
        if (i != n):
            output += letter
        i += 1
    return (output)
