#!/usr/bin/python3
#8-class_to_json.py
"""defines a class to json function
"""
def class_to_json(obj):
    """returns the dictionary description with simple 
       data structure (list, dictionary, string, integer
       and boolean) for JSON serialization of an object:

    Args:
        obj (object): the object in the class

    Returns:
        any: dictionary description
    """    
    return obj.__dict__