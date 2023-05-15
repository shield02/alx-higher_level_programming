#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    out_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            out_list.append(False)
        else:
            out_list.append(True)
    return out_list
