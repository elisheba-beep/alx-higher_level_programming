#!/usr/bin/python3
#5-save_to_json_file.py
"""defines a save to json file function
"""
def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation:

    Args:
        my_obj (any): the data to be written to the json file
        filename (string): the name of the file to write to

    Returns:
        any: the created file with the data
    """    
    import json
    with open(filename, mode="w", encoding="utf-8") as f:
        save = f.write(json.dumps(my_obj))
        return save