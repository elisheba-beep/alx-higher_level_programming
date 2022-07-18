#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number = 0
    for item in my_list[:x]:
        try:
            print("{:d}".format(item), end="")
            number = number + 1
        except (ValueError, TypeError):
            continue
    print("")
    return (number)
