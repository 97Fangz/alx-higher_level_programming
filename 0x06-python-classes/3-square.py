#!/usr/bin/python3
"""class Square"""


class Square:
    """Represents a square

    Attribute:
        _size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the squar

        Args:
            size (int): size of a side of the square

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self._size = size

    def area(self):
        """calculates the square's area

        Returns:
            The area of the square
        """
        return (self._size) ** 2
