#!/usr/bin/python3
#0-read_file.py
"""defines a function
"""
def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:

    Args:
        filename (str, optional): The path to the file needed to be opened.
        Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")