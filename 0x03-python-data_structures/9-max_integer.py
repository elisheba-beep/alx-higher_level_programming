#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    highest_num = my_list[0]
    for number in range len(my_list):
        if my_list[number] > highest_num:
            highest_num = my_list[number]
    return (highest_num)
