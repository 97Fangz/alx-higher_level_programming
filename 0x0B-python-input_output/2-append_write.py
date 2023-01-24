#!/usr/bin/python3
"""Module append_write. Contains the function append_write
"""


def append_write(filename="", text=""):
    """Appends text to filename.

    Args:
        filename: name of the file
        text: text to append

        Return: the number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
