#!/usr/bin/python3
"""class MyList that inherits from list
"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted in asc order
        """
        print(sorted(self))
