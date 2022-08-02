#!/usr/bin/python3
#6-load_from_json_file.py
"""defines an object creation function
"""
def load_from_json_file(filename):
    """creates an Object from a “JSON file”:

    Args:
        filename (string): the name of the file with the data

    Returns:
        object: the python object created
    """    
    import json
    with open(filename, "r", encoding="utf-8") as f:
        save = json.load(f)
        return save