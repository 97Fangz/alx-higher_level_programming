#!/usr/bin/python3
"""Module is_kind_of_class. To find the instance of object of instance of a
class
"""


def is_kind_of_class(obj, a_class):
    """Finds if obj is an instance of a_class or a class inherited from a_class

    Args:
        obj: object to look at
        a_class: class to evaluate

        Returns: True of False
    """

    return isinstance(obj, a_class)
