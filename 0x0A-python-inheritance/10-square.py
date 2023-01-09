#!/usr/bin/python3
"""Square class that imports from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""

    def __init__(self, size):
        """Method that initializes Square Class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
