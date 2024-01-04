#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width : int = 0, height : int = 0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of rectangle

        Args:
            value (int) : the new width of the rectangle

        Raises:
            TypeError : If the value is not integer
            ValueError : If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get the height """
        return self.__height

     @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return the area of rec """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Returns the perimeter

        Returns : 
            int : permiter
        
        Raises:
            ValueError: If the width or height of the rectangel is zero
        """
        if self.__width == 0 or self.__height = 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ return the printable representation of rec
            represent rect with '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []

        for i in range(self.__height):
            # add '#' for each row
            [rect.append('#') for j in range(self.__width)]
            # add new line character
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)
