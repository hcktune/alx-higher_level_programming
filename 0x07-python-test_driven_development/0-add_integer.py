#!/usr/bin/python3

"""

This module is composed by a function that adds two numbers

"""

def add_integer(a, b=98):
	""" Function that adds two integers must be int or float

	Args : 
		a: num1
		b: num2

	Returns:
		the addition of the two numbers

	Raises:
		TypeError: If a or b aren't int and/or float
	
	"""

	  if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer and/or float")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer and/or float")
    a = int(a)
    b = int(b)
    return (a + b)
