#!/usr/bin/env python3
i = 0
for i in range(ord('a'), ord('z') + 1):
    lettre = chr(i)
    if lettre != 'q' and lettre != 'e':
        print(lettre, end="")
print()
