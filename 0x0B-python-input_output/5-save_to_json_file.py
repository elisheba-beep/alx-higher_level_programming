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
    
def main():
    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "my_dict.json"
    my_dict = { 
        'id': 12,
        'name': "John",
        'places': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename)

    try:
        filename = "my_set.json"
        my_set = { 132, 3 }
        save_to_json_file(my_set, filename)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
main()