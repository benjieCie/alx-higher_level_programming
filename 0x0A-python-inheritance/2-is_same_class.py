#!/usr/bin/python3
def is_same_class(obj, a_class):
    """function that returns True if the object is exactly
    an instance of the specified clas otherwise False"""
    return (type(obj) == a_class)
