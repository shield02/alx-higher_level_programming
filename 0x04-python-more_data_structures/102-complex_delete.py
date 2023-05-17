#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if (value not in a_dictionary.values()):
        return a_dictionary
    if (a_dictionary is None) or (len(a_dictionary) == 0):
        return a_dictionary
    
    for key in a_dictionary.copy():
        if value == a_dictionary[key]:
            del a_dictionary[key]
    return a_dictionary
