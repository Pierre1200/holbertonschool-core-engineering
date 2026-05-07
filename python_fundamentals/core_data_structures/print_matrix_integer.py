#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):

    for lignes in matrix:
        for i in range(len(lignes)):
            print("{:d}".format(lignes[i]), end="")
            if i < len(lignes) - 1:
                print(" ", end="")
        print()
