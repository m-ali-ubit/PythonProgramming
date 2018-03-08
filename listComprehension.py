
from math import sqrt
# list comprehension is a quick way of making a list

# list of squares of numbers from 0 to 10
print([n ** 2 for n in range(11)])

# list of cubed of numbers from 0 to 10
print([n ** 3 for n in range(11)])

# list of multiple of 2 of numbers from 0 to 10
print([n * 2 for n in range(11)])

# list of even number from 0 to 20
print([n for n in range(21) if not n % 2])

# extract list of positive numbers from a list
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print([int(x) for x in numbers if x > 0])

# list of all numbers from 1 to 100 that are divisible by 7
print([n for n in range(101) if n % 7 == 0])

# list of all numbers from 1 to 100 that have 3 in them
print([n for n in range(100) if '3' in list(str(n))])

# list of all characters of string except vowels
string = 'The Quick Brown Fox Jumped Over The Lazy Dog'
s = [char for char in string if char not in 'aeiou']
print(s)
print(''.join(s))   # list to string conversion

# list of all the capital letters in a string
print([char for char in string if char.isupper()])

# list of negative numbers from 10 to 1
print([n for n in range(-10, 0)])

# nested comprehension
# list of tuples and each tuple contains digit and its square
sample = [1, 2, 3, 4]
print([(sample[a], sample[b]**2) for a in range(len(sample)) for b in range(a, len(sample))])

# generate pythagorean triple a^2 + b^2 = c^2
pairs = [(a, b, sqrt(a**2 + b**2)) for a in range(1, 11) for b in range(a, 11)]
print(pairs)
# this will filter out all non pythagorean triples
pairs = list(filter(lambda triple: triple[2].is_integer(), pairs))
print(pairs)

# simple pythagorean triple using comprehension ; a better one
pairs = [(a, b, sqrt(a**2 + b**2)) for a in range(1, 11) for b in range(a, 11)]
pairs = [(a, b, int(c)) for a, b, c in pairs if c.is_integer()]
print(pairs)

# list of all numbers from 1 to 100 that are divisible by any single digit
print([n for n in range(1, 101) if [d for d in range(2, 11) if n % d == 0]])
