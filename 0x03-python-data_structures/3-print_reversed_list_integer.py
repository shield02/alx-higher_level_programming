#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    if my_list is None:
        return
    for i in range(1, n+1):
        print('{:d}'.format(my_list[-i]))
