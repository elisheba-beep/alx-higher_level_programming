#!/usr/bin/python3
def comb3(a, b):
    t = []
    t.append(a)
    t.append(b)
    for i in range(0,2):
        for j in range(0,2):
            if(i != j ):
                print("{:s}".format(t[i]+ t[j]))
                

