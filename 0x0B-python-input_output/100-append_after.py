#!/usr/bin/python3
"""a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """INserts a line of test to a file containing a specific string"""
    text = ""
    with open(filename) as a_file:
        for line in a_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as another_file:
        another_file.write(text)
