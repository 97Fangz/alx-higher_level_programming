#!/usr/bin/python3
"""Module add_attribute. Adds another attribute.
"""


def add_attribute(an_obj, an_attr, a_value):
    """Checks if an_attr of value a_value can be added to an_obj."""

    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(an_obj, '__slots__') and not hasattr(an_obj, an_attr):
        raise TypeError("can't add new attribute")

    setattr(an_obj, an_attr, a_value)