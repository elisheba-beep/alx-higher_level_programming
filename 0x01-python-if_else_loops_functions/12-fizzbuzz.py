#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("{:s}".format("FizzBuzz"), end=" ")
            continue
        elif (i % 5 == 0):
            print("{:s}".format("Buzz"), end=" ")
            continue
        elif (i % 3 == 0):
            print("{:s}".format("Fizz"), end=" ")
            continue
        print("{:d}".format(i), end=" ")
