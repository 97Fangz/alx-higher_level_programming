#!/usr/bin/python3
"""Module rectangle. Initializes instation
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle. Private instance attributes of width and height
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes an instance of width and height of the rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
