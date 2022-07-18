#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number = 0
    for item in range(0, x):
        try:
            print("{:d}".format(my_list[item]), end="")
            number = number + 1
        except (ValueError, TypeError):
            continue
    print("")
    return (number)
