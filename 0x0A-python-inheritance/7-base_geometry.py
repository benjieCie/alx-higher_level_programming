#!/usr/bin/python3
"""A base Geometry class"""


class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """Area not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates a value as int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
