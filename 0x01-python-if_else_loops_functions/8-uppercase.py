#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        i = ord(i) - 32
        new_str = new_str + chr(i)
    print("{:s}".format(new_str))
