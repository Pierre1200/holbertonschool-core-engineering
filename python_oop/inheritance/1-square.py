#!/usr/bin/env python3
""" Module BaseGeometry """
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """classe square"""
    def __init__(self, size):
        """Init de la forme"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calcul de l'aire"""
        return self.__size * self.__size
