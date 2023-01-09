#!/usr/bin/python3
"""
    Returns list of available attributes
    and methods of an object
"""


def lookup(obj):
    """unction that returns the list of available 
    attributes and methods of an object"""
    return dir(obj)
