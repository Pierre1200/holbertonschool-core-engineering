#!/usr/bin/env python3
"""Module d'écriture"""


def write_file(filename="", text=""):
    """Fonction d'écriture"""
    with open(filename, "w", encoding="utf-8") as filename:
        filename.write(text)
