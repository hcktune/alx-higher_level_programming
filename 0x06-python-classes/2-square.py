#!/usr/bin/python3

""" size of validation """


class Square:
    """ class Square that defines a square"""
    def __init__(self, size = 0):
         """initialize square
        Args:
            size (int): size must be integer 
        """
        if type(size) is not int:
            raise TypeError('size must be int')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
