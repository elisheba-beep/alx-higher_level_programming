#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """searches my_list for the element
    search and replaces it with replace"""
    result = [replace if i == search else i for i in my_list]
    return (result)
