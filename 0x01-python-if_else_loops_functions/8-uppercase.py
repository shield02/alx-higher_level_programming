#!/usr/bin/python3
def uppercase(str):
    str_list = list(str)
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            str_list[i] = chr(ord(str[i]) - 32)
    print("{}".format("".join(str_list)))
