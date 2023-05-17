#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    o_dict = dict(sorted(a_dictionary.items()))
    for key, value in o_dict.items():
        print("{}: {}".format(key, value))
