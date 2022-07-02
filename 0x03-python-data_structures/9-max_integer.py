#!/usr/bin/python3
def max_integer(my_list=[]):
    highest_num = 0
    if len(my_list) == 0:
        return ("None")
    for number in my_list:
        if number > highest_num:
            highest_num = number
    return (highest_num)
