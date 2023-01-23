#!/usr/bin/python3
"""Module base_geometry. Finding public instance methods.
"""


class BaseGeometry:
    """Class BaseGeometry."""

    def area(self):
        """area of the geometry"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """value: the one to validated"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))