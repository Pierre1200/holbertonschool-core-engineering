#!/usr/bin/env python3

resultat = ""
for i in range(ord('a'), ord('z') + 1):
    lettre = chr(i)
    if lettre != 'q' and lettre != 'e':
        resultat += lettre
print("{}".format(resultat), end="")
