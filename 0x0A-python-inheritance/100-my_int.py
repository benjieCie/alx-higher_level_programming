#!/usr/bin/python3
"""Rebel Class that inherits from int"""


class MyInt(int):
    """Rebel Class that inverts == and != operators"""

    def __eq__(self, value):
        """Change == operator to != operator"""
        return self.real != value

    def __ne__(self, value):
        """change != operato to == operator"""
        return self.real == value
