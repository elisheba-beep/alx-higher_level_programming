#!/usr/bin/python3
def print_last_digit(number):
    num = repr(number)
    last_digit_string = num[-1]
    last_digit = int(last_digit_string)
    print("{:d}".format(last_digit), end="")
    return last_digit
