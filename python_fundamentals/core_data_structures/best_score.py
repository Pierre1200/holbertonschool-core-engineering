#!/usr/bin/env python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    la_plus_grosse = max(a_dictionary, key=a_dictionary.get)
    return la_plus_grosse
