#!/usr/bin/python3
"""find a peak"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[:]
    if len(list_of_integers) == 2:
        return max(list_of_integers)

    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
