#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None) or (len(a_dictionary) == 0):
        return None
    else:
        values = list(a_dictionary.values())
        keys = list(a_dictionary.keys())
        hghst_val = values.index(sorted(values)[-1])
    return (keys[hghst_val])
