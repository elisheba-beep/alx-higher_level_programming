#!/usr/bin/python3
def remove_char_at(str, n):
    copy = str[:]
    if (len(copy) > n):
        copy = copy[0 : n : ] + copy[n + 1 : :]
    return copy
