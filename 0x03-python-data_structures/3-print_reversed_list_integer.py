#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    if my_list is None or my_list == []:
        return None
    for i in reversed(my_list):
        print('{:d}'.format(i))
