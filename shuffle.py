from string import ascii_uppercase
from random import shuffle

n = int(input())
x = list(ascii_uppercase[:n])
shuffle(x)

print()
for c in x:
    print(c)