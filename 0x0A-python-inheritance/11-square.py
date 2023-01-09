#!/usr/bin/python3
"""Square class that inherits rom Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectablge"""

    def __init__(self, size):
        """Initialize the Square Class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
