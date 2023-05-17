#!/usr/bin/python3
def weight_average(my_list=[]):
    denominator = 0
    numerator = 0
    for tup in my_list:
        denominator += tup[1]
        numerator += (tup[0] * tup[1])
    w_avg = numerator/denominator
    return w_avg
