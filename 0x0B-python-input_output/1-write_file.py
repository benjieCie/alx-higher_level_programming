#!/bin/usr/python3
"""A function that writes a string to a text and returns no of chars"""


def write_file(filename="", text=""):
    """Writes to a file and returns number of chars"""
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
