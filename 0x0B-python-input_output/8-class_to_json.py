#!/usr/bin/python3
"""returns the dictionary description for
JSON serialization of an object"""


def class_to_json(obj):
    """Returns dictionary representation of a JSON sirialization object"""
    return obj.__dict__
