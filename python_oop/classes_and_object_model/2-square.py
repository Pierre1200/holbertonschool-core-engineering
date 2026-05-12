#!/usr/bin/env python3
"""
Module docstring: explique ce que fait ce module.
"""


class Square:
    """
    Class docstring: explique ce qu'est un carré ici.
    """

    def __init__(self, size=0):
        """
        Initialise le carré.

        Args:
            size (int): La taille du carré.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
