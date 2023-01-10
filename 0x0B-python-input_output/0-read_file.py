#!/usr/bin/python3
"""A fintion that read a txt file and prints to std out"""


def read_file(filename=""):
    """Read test file and prints on stdout"""
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
