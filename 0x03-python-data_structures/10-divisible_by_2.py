#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    res = []
    for num in my_list:
       divisible_by_2 = num % 2 == 0
       res.append(divisible_by_2)
    return res
