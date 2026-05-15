#!/usr/bin/env python3
"""
Module explorant l'héritage multiple avec Fish, Bird et FlyingFish
"""


class Fish:
    """Classe représentant un poisson"""

    def swim(self):
        """Affiche le comportement de nage"""
        print("The fish is swimming")

    def habitat(self):
        """Affiche l'habitat du poisson"""
        print("The fish lives in water")


class Bird:
    """Classe représentant un oiseau"""

    def fly(self):
        """Affiche le comportement de vol"""
        print("The bird is flying")

    def habitat(self):
        """Affiche l'habitat de l'oiseau"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe FlyingFish héritant à la fois de Fish et de Bird.
    Démontre l'héritage multiple et la surcharge de méthodes.
    """

    def fly(self):
        """Surcharge du vol pour le poisson volant"""
        print("The flying fish is soaring!")

    def swim(self):
        """Surcharge de la nage pour le poisson volant"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Surcharge de l'habitat pour le poisson volant"""
        print("The flying fish lives both in water and the sky!")
