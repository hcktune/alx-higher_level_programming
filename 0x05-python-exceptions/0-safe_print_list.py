#!/usr/bin/python

def safe_print(my_list=[], x=0):
    res = 0
    for i in range(my_list):
        try:
            print("{}".format(my_list[i], end="")
            res += 1
        except IndexError:
                  break
    print('')
    return(res)
