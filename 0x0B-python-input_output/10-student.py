#!/usr/bin/python3
"""Module student. Main class"""


class Student:
    """main class that contains the functions"""

    def __init__(self, first_name, last_name, age):
        """returns the details of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json"""
        dic = {}
        if attrs is None:
            return self.__dict__
        for a in attrs:
            if hasattr(self, a):
                dic[a] = getattr(self, a)
        return dic
