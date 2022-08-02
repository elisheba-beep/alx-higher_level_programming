#!/usr/bin/python3
#4-from_json_string.py
"""defines a function to get an object from a json string
"""
def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string:

    Args:
        my_str (any): the json string to be converted to a python object

    Returns:
        any: the python object
    """    
    import json
    my_string = json.loads(my_str)
    return my_string