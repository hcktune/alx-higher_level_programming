#!/usr/bin/python3

""" add attributes to the square class """


class Square:
    """ class Square that defines a square"""
    def __init__(self, size):
         """initialize square
        Args:
            size (int): size of the square
        """
        self.__size = size
