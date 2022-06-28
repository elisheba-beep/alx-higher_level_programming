#!/usr/bin/python3
def uppercase(str):
    for i in range(97,123):
        if (ord(i) == str[i]):
                i = i + 32
                print("{:s}".format(str[i]))
