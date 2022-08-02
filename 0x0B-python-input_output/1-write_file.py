#!/usr/bin/python3
#1-write_file.py
"""defines a write function
"""
def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of characters written:

    Args:
        filename (str, optional): The path to the file to write to or 
        the name of the newfile to create. Defaults to "".
        text (str, optional): The text to be written in that file. Defaults to "".

    Returns:
        number: the number of characters written.
    """    
    with open(filename, mode="w", encoding="utf-8") as f:
        write_line = f.write(text)
        return write_line