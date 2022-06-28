#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = repr(number)
last_digit_string = num[-1]
last_digit = int(last_digit_string)
if (number < 0):
    last_digit = last_digit * -1
if (last_digit > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, last_digit))
elif (last_digit == 0):
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))
elif (last_digit < 6 and last_digit != 0):
    print("Last digit of {:d} is {:d} "
          "and is less than 6 and not 0".format(number, last_digit))
