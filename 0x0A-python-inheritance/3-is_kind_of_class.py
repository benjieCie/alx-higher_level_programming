#!/usr/bin/python3
"""checks if object is an instance of, or if the object
is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """Returns True if objecy is an instance of a class,
    or if object is an instance of a class that inherited
    otherwise False"""

    return (isinstance(obj, a_class))
