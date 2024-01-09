#!/usr/bin/python3

""" module contains a function that writes a string to text file """

def write_file(filename="", text=""):
    """  writes to a text file

    Args:
        filename: name of file to write to
        text: content
    
    Raises:
        Exceptions: Raises an exception

    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
