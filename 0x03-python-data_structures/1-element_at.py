#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)

    while True:
        if(idx < 0):
            return None
        elif(idx > list_len):
            return None
        else:
            return int(my_list[idx])
