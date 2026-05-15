#!/usr/bin/env python3
""" Module BaseGeometry """


class BaseGeometry:
    """Classe BaseGeometry"""
    def area(self):
        """ Définit l'aire """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Valide si value est un entier strictement positif """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Classe rectangle"""
    def __init__(self, width, height):
        """Init du rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
