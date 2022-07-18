#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    for item in my_list[:x]:
        try:
            number = number + 1
            print('{}'.format(item), end='')
        except IndexError:
            break
    print('')
    return (number)
