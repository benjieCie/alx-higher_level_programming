#!/usr/bin/python3
"""A student class that defines a student"""


class Student:
    """Represents a Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary rep of the Class student
        If attrs is a list of strings"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
