#!/usr/bin/env python3
""" Module docstring """


class Square:
    """ Class docstring """

    def __init__(self, size=0):
        """ Initialise le carré """
        self.size = size

    @property
    def size(self):
        """ Getter : Récupère la taille """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter : Modifie la taille avec validation """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calcule l'aire (utilise self.__size) """
        return self.__size ** 2

    def my_print(self):
        """
        Imprime le carré avec le caractère #.
        Si la taille est 0, imprime une ligne vide.
        """
        if self.size == 0:
            print()
            return

        for i in range(self.size):
            print("#" * self.size)
