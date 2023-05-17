#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for elem_tuple in list(enumerate(my_list)):
        if elem_tuple[1] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[elem_tuple[0]])
    return new_list
