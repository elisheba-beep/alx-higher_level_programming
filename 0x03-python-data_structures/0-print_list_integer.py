#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        """prints a list of integers"""
        for i in range(0, len(my_list)):
            print("{}".format(my_list[i]))