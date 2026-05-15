#!/usr/bin/env python3
"""
Module définissant une classe abstraite Animal et ses subclasses
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe de base abstraite représentant un animal
    """

    @abstractmethod
    def sound(self):
        """
        Méthode abstraite que chaque sous-classe doit implémenter
        """
        pass


class Dog(Animal):
    """
    Classe concrète représentant un chien
    """

    def sound(self):
        """
        Implémentation du cri du chien
        """
        return "Bark"


class Cat(Animal):
    """
    Classe concrète représentant un chat
    """

    def sound(self):
        """
        Implémentation du cri du chat
        """
        return "Meow"