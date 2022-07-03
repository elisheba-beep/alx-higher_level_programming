#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    highest_num = 0
    for number in my_list:
        if number > highest_num:
            highest_num = number
    return (highest_num)
