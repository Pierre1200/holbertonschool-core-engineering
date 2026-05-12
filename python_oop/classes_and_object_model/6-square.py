#!/usr/bin/env python3
""" Module docstring """


class Square:
    """ Class docstring """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialise le carré """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Getter : Récupère la position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter : Récupère la position """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calcule l'aire (utilise self.__size) """
        return self.__size ** 2

    def __str__(self):
        if self.size == 0:
            return ""

        res = []
        for _ in range(self.position[1]):
            res.append("")

        for _ in range(self.size):
            res.append(" " * self.position[0] + "#" * self.size)

        return "\n".join(res)

    def my_print(self):
        """ Affiche le carré """
        if self.size == 0:
            print()
        else:
            print(self)
