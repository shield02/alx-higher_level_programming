#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    result = 0
    if my_list is None:
        return 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            result = result + 1
        except (ValueError, TypeError, IndexError):
            pass
    print()
    return result
