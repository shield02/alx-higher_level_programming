#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    if my_list is None:
        return 0
    try:
        while i < x:
            print("{:d}".format(my_list[i]), end="")
            i = i + 1
        print()
    except IndexError:
        print()
        pass
    return i
