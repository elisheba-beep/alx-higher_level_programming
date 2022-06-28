#!/usr/bin/python3
def uppercase(str):
    for i in range(ord('a'), ord('z') + 1):
        for j in range(ord('A'), ord('Z') + 1):
            str[i] = str[j]
            print("{:s}".format(str))
