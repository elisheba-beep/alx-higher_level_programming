#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """print different"""
    diff1 = [i for i in set_1 if i not in set_2]
    diff2 = [i for i in set_2 if not i in set_1]
    diff = diff1 + diff2
    return (diff)
