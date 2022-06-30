#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """gives the addition of all arguments"""
    add = 0
    for i in range(1, len(sys.argv)):
        a = int(sys.argv[i])
        add += a
    print(add)
