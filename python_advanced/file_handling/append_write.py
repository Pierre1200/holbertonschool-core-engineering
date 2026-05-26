#!/usr/bin/env python3
"""Module d'ajout"""


def append_write(filename="", text=""):
    """Fonction d'ajout"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
