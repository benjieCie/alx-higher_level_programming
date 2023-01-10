#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """A function that appends a string at the end
    of a text file and returns no of chars"""
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
