#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """A square class with private attribute size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates area of a square object"""
        return (self.__size * self.__size)

    def print_position(self):
        """Returns Spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for x in range(self.position[1]):
            pos += "\n"
        for x in range(self.size):
            for i in range(sef.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """Prints stdout the square with the character #"""
        print(self.pos_print(), end="")
