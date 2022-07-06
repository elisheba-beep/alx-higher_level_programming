#!/usr/bin/python3
def best_score(a_dictionary):
    """key with the highest int"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)
    res = list(a_dictionary.keys())[0]
    high = a_dictionary[res]
    for k, v in a_dictionary.items():
        if v > high:
            high = v
            res = k
    return (res)
