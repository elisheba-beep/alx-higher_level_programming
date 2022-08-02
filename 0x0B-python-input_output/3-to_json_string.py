#!/usr/bin/python3
#3-to_json_string.py
"""defines a json representation function
"""
def to_json_string(my_obj):
    """ returns the JSON representation of an object (string):

    Args:
        my_obj (any): The object to be represented

    Returns:
        any: the json representation
    """    
    import json
    string = json.dumps(my_obj)
    return string