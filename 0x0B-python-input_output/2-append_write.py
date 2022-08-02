#!/usr/bin/python3
#2-append_write.py
"""defines an append function
"""
def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) 
       and returns the number of characters added:

    Args:
        filename (str, optional):The name of the file to be changed.
        Defaults to "".
        text (str, optional): The text to be appended to the file.
        Defaults to "".

    Returns:
        number: The number of characters in the file
    """    
    with open(filename, mode="a", encoding="utf-8") as f:
        append_line = f.write(text)
        return append_line