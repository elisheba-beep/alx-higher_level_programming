#!/usr/bin/python3
def no_c(my_string):
    remove = ['c', 'C']
    new_string = "".join([i for i in my_string if i not in remove])
    return (new_string)
