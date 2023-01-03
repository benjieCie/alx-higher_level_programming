#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Init the rectanlge class
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width attribute"""
        return self.__width

    @property
    def height(self):
        """Gets height attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle object"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of a rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns string representation of rectanlge object"""
        rep_str = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for col in range(self.__height):
            for row in range(self.__width):
                rep_str += "#"
            if col < self.__heiht - 1:
                rep_str += "\n"
        return (rep_str)

    def __repr__(self):
        """Return rep of Rectangle that can be used by eval() to 
        create new object"""
        rec_str = "Rectangle(" + str(self.__width) + "," + str(self.__height) + ")"
        return rec_str
