#!/usr/bin/python3
for i in range(0,10):
    for j in range(i + 1,10):
        if (i != j):
            i = str(i)
            j = str(j)
            print("{:s}".format(i+j), end=", ")
        continue
    continue
