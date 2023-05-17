#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    values = list(a_dictionary.values())
    if value not in values:
        return a_dictionary
    try:
        for key in a_dictionary.copy():
            if value == a_dictionary[key]:
                del a_dictionary[key]
        return a_dictionary
    except KeyError:
        return a_dictionary
