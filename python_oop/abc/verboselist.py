#!/usr/bin/env python3
"""
Module définissant VerboseList, une extension de la classe native list
"""


class VerboseList(list):
    """
    Une liste qui notifie l'utilisateur lors de chaque modification.
    """

    def append(self, item):
        """Ajoute un élément et affiche un message"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Étend la liste et affiche le nombre d'éléments ajoutés"""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Affiche un message PUIS retire l'élément"""
        # Note: On affiche AVANT car si l'item n'est pas là, 
        # super().remove lèvera une erreur et le print ne s'exécutera pas.
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Affiche l'élément qui va être retiré via pop,
        puis appelle la méthode parente.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
