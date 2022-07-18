#!/usr/bin/python3
''''prints items in a list oon one line
and returns the number of items printed'''
def safe_print_list(my_list=[], x=0):
    number = 0
    for item in my_list[:x]:
        try:
            number = number + 1
            print(item, end='')
        except (RuntimeError, TypeError, ValueError):
            print ("error")
    print('\n')
    return (number)
