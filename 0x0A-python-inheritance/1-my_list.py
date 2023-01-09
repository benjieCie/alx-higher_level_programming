#!/usr/bin/python3
"""This Class inherits from the list class"""


class MyList(list):
    """Inherits from list class"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
