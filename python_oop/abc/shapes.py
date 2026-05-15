#!/usr/bin/env python3
"""
Module définissant une classe abstraite Shape et le concept de Duck Typing
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe de base abstraite pour les formes géométriques
    """

    @abstractmethod
    def area(self):
        """ Calcule l'aire de la forme """
        pass

    @abstractmethod
    def perimeter(self):
        """ Calcule le périmètre de la forme """
        pass


class Circle(Shape):
    """
    Représente un cercle
    """

    def __init__(self, radius):
        """ Initialisation avec le rayon """
        self.radius = radius

    def area(self):
        """ Aire : pi * r^2 """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """ Périmètre : 2 * pi * r """
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Représente un rectangle
    """

    def __init__(self, width, height):
        """ Initialisation avec largeur et hauteur """
        self.width = width
        self.height = height

    def area(self):
        """ Aire : L * l """
        return self.width * self.height

    def perimeter(self):
        """ Périmètre : 2 * (L + l) """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Fonction qui illustre le Duck Typing.
    Elle appelle area() et perimeter() sans vérifier le type de l'objet.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
