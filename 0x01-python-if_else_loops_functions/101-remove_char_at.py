#!/usr/bin/python3
def remove_char_at(str, n):
    copy = str[:]
    copy = copy[:n] + copy[n + 1:]
    return copy
