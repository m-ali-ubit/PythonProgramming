
# dictionary comprehension is the quick way to make dictionaries like lists

from string import ascii_lowercase
import os
# print(dict((c, k) for k, c in enumerate(ascii_lowercase, 1)))
# print({(c, k) for k, c in enumerate(ascii_lowercase, 1)})

d1 = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
d2 = {(c, k) for k, c in enumerate(ascii_lowercase, 1)}
d3 = dict(sorted({(c, k) for k, c in enumerate(ascii_lowercase, 1)}))
d4 = {c: k for k, c in enumerate(ascii_lowercase, 1)}
d5 = {k: v for (k, v) in zip(ascii_lowercase, range(1, 27))}

print(d1)           # prints letters as key and their positions as a value
print(d2)           # prints unsorted dict of tuples of letters and value
print(d3)           # pass d2 from sorted, returns sorted list of tuples and dict() type cast list to dictionary
print(d4)           # to do same as dict() comprehension ; change (c,k) to c : k
print(d5)
print(d1 == d2)     # False
print(d1 == d3)     # True
print(d1 == d4)     # True
print(d1 == d5)     # True
