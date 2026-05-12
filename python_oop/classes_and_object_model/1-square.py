#!/usr/bin/env python3
"""
Module 1-square
Définit une classe Square avec un attribut de taille privé.
"""


class Square:
    """
    Représente un carré.

    Attributes:
        __size (int): La taille d'un côté du carré.
    """

    def __init__(self, size):
        """
        Initialise une nouvelle instance de Square.

        Args:
            size (int): La taille du carré.
        """
        self.__size = size