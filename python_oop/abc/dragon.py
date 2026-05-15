#!/usr/bin/env python3
"""
Module démontrant l'utilisation des Mixins pour composer des comportements
"""


class SwimMixin:
    """Mixin pour ajouter la capacité de nager"""

    def swim(self):
        """Affiche le comportement de nage du mixin"""
        print("The creature swims!")


class FlyMixin:
    """Mixin pour ajouter la capacité de voler"""

    def fly(self):
        """Affiche le comportement de vol du mixin"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Classe Dragon composée via Mixins.
    Le Dragon n'est pas "un vol", il possède la "capacité de voler".
    """

    def roar(self):
        """Méthode spécifique à la classe Dragon"""
        print("The dragon roars!")
