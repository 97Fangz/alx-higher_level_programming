#!/usr/bin/python3
"""Module write_file. Contains the function write_file
"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the number of characters
    written.

    Args:
        filename: name of the file
        text: string to write in the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
