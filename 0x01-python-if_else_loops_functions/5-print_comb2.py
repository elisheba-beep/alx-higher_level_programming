#!/usr/bin/python3
for num in range(0, 100):
    if (num < 10):
        num = "0" + str(num)
        print("{:s}, ".format(num), end="")
        continue
    if (num == 100):
        break
    print("{:d}, ".format(num), end="")
