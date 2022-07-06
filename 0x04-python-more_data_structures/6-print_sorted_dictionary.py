#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictionary = sorted(a_dictionary.keys(), key = lambda x: x.upper())
    for k in dictionary:
        v = a_dictionary[k]
        print("{}: {}".format(k, v))
    return (k, v)
