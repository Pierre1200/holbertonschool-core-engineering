#!/usr/bin/env python3
"""Module de lecture"""


def read_file(filename=""):
    """Fonction de lecture"""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
