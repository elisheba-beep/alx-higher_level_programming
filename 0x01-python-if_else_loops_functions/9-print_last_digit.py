#!/usr/bin/python3
def print_last_digit(number):
    num = repr(number)
    last_digit_string = num[-1]
    last_digit = int(last_digit_string)
    if (number < 0):
        last_digit = last_digit * -1
    print("{:d}".format(last_digit), end="")
    return last_digit
