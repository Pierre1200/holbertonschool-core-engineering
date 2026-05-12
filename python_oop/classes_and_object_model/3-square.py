#!/usr/bin/env python3
"""
Module docstring
"""


class Square:
    """
    Class docstring
    """

    def __init__(self, size=0):
        """
        Initialise le carré avec validation (reprend ton code précédent).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            L'aire (size * size)
        """
        return self.__size * self.__size
