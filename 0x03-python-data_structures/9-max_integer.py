#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_tmp = my_list[0]
        for i in my_list:
            if i > max_tmp:
                max = i
        return max
